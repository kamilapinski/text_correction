from metrics import calculate_accuracy, calculate_f1, calculate_precision, calculate_recall
from transformers import pipeline

spell_checker = pipeline("text2text-generation", model="t5-base")

def correct_spelling(text):
    input_text = f"correct: {text}"
    corrected_text = spell_checker(input_text, max_length=512, num_return_sequences=1)[0]['generated_text']
    
    corrected_text = corrected_text.replace('- (FR)', '').strip()
    
    return corrected_text