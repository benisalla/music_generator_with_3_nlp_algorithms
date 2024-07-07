import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim.lr_scheduler import CosineAnnealingLR
from music_generator.core.config import MGConfig
from music_generator.model.MGTransformer import MGTransformer
from music_generator.data.dataloader import DataLoader
from music_generator.model.utils import live_plot_dual, save_checkpoints, train_epoch, validate_epoch
from music_generator.tokenizing.tokenizer.MGTokenizer import MGTokenizer
import matplotlib.pyplot as plt
import gc


# Build configs
mgconfig = MGConfig()

# Data paths
main_dir = "./music_generator/src"
train_path = f'{main_dir}/dataset/train_abc.json'
val_path = f'{main_dir}/dataset/val_abc.json'
load_tokenizer_path = f"{main_dir}/tokenizer/mgt_tokenizer_v1.model"  

print("Loading the data...")
data_loader = DataLoader(train_path, val_path)

# Load and preprocess data
train_text, val_text = data_loader.get_data()
print(f"Train text sample: {train_text[:10]}")
print(f"Val text sample: {val_text[:10]}")

# Initialize and load tokenizer
tokenizer = MGTokenizer()
tokenizer.load(load_tokenizer_path)

mgconfig.v_size = len(tokenizer.vocab)
mgconfig.set_train_size(len(train_text))

# Hyperparameters
lr_rate = mgconfig.lr_rate
beta1, beta2 = mgconfig.beta1, mgconfig.beta2
eps = mgconfig.eps
w_decay = mgconfig.w_decay
num_epochs = mgconfig.num_epochs
min_lr = mgconfig.min_lr
device = mgconfig.device
label_smoothing = mgconfig.label_smoothing
n_embd = mgconfig.n_embd
h_dim = mgconfig.h_dim
n_block = mgconfig.n_block
v_size = mgconfig.v_size
b_size = mgconfig.b_size
max_seq_len = mgconfig.max_seq_len
ff_dim = mgconfig.ff_dim
drop_rate = mgconfig.drop_rate
bias = mgconfig.bias
n_step = mgconfig.n_step
seq_len = mgconfig.seq_len
save_ckpt_path = mgconfig.save_ckpt_path

# MGTransformer model
model = MGTransformer(
    n_embd=n_embd,
    h_dim=h_dim,
    n_block=n_block,
    v_size=v_size,
    b_size=b_size,
    max_seq_len=max_seq_len,
    ff_dim=ff_dim,
    drop_rate=drop_rate,
    bias=bias,
)

# Loss function
criterion = nn.CrossEntropyLoss(label_smoothing=label_smoothing)

# Optimizer
optimizer = optim.AdamW(
    model.parameters(),
    lr=lr_rate,
    betas=(beta1, beta2),
    eps=eps,
    weight_decay=w_decay
)

# Scheduler
scheduler = CosineAnnealingLR(optimizer, T_max=num_epochs, eta_min=min_lr)

# Tokenize data
train_tokens = tokenizer.encode(train_text[:10000])
val_tokens = tokenizer.encode(val_text[:2000])

print(f"len(train_tokens) : {len(train_tokens)}")
print(f"len(val_tokens) : {len(val_tokens)}")

# Start training
train_losses, train_accs, train_perplexities = [], [], []
val_losses, val_accs, val_perplexities = [], [], []

model.to(device)
curr_lr = optimizer.param_groups[0]['lr']

for epoch in range(num_epochs):
    t_loss, t_acc, t_perplexity = train_epoch(model, train_tokens, optimizer, seq_len, b_size, n_step, device)
    v_loss, v_acc, v_perplexity = validate_epoch(model, val_tokens, seq_len, b_size, n_step, device)

    if epoch % 5 == 0 and epoch > 0:
        scheduler.step()
        curr_lr = optimizer.param_groups[0]['lr']

        train_losses.append(t_loss)
        train_accs.append(t_acc)
        train_perplexities.append(t_perplexity)

        val_losses.append(v_loss)
        val_accs.append(v_acc)
        val_perplexities.append(v_perplexity)

        plt.close('all')
        data_dict = {
            'Train Loss': train_losses,
            'Val Loss': val_losses,
            'Train Acc': train_accs,
            'Val Acc': val_accs,
            'Train Perplexity': train_perplexities,
            'Val Perplexity': val_perplexities
        }
        live_plot_dual(data_dict, title=f'Training & Validation Metrics [lr={curr_lr:.7f}]')

        # torch.cuda.empty_cache()
        # gc.collect()

    if epoch % 100 == 0 and epoch > 0:
        save_checkpoints(model, optimizer, save_ckpt_path)
