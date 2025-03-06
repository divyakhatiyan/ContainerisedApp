from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
conversation_history = []

model_name = "facebook/blenderbot-400M-distill"

# Load model (download on first run and reference local installation for consequent runs)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

while True:

    history_string = "\n".join(conversation_history)

    input_text ="hello, how are you doing?"

    inputs = tokenizer.encode_plus(history_string, input_text, return_tensors="pt")
    tokenizer.pretrained_vocab_files_map

    print(inputs)

    outputs = model.generate(**inputs)
    print(outputs)

    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    print(response)

    conversation_history.append(input_text)
    conversation_history.append(response)
    print(conversation_history)