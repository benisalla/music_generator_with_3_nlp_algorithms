from music_generator.data.dataloader import DataLoader
from music_generator.tokenizing.tokenizer import KerasTokenizer

main_dir = "./music_generator/src"

train_path = f'{main_dir}/dataset/train_abc.json'
val_path = f'{main_dir}/dataset/val_abc.json'
save_path = f"{main_dir}/tokenizer/mgt_tokenizer_test"

print("loading the data ...")
data_loader = DataLoader(train_path, val_path)

# Load and preprocess data
train_text, val_text = data_loader.get_data()
print(f"train text: {train_text[:10]}")
print(f"val text: {val_text[:10]}")

vocab_size = 1000


tokenizer = KerasTokenizer(num_words=vocab_size, oov_token="<OOV>")
print("Training the tokenizer...")
tokenizer.fit([val_text])  


word_index = tokenizer.get_word_index()
max_index = max(word_index.values())  

special_tokens = {
    "<PAD>": max_index + 1,
    "<SOS>": max_index + 2,
    "<EOS>": max_index + 3
}
tokenizer.tokenizer.word_index.update(special_tokens)  


sequence = tokenizer.texts_to_sequences(["gfeg fd d2 | eaaf gedB ||<EOS>"])
print("Tokenized sequence:", sequence)


vocab_size = tokenizer.get_vocab_size()
print("Vocabulary size:", vocab_size)

# Save the tokenizer
print("Saving the tokenizer...")
tokenizer.save(save_path)
print(f"Tokenizer successfully saved at {save_path}.")
