from random_mistaker import introduce_typos_to_text
from spell_checker import correct_spelling
from metrics import calculate_accuracy, calculate_f1, calculate_precision, calculate_recall

def load_sentences(file_path):
    with open(file_path, 'r') as file:
        sentences = file.readlines()
    return [sentence.strip() for sentence in sentences]

def main():
    correct_sentences = load_sentences('correct_sentences.txt')
    
    original_words_list = []
    corrected_words_list = []

    summary_accuracy = 0
    summary_precision = 0
    summary_recall = 0
    summary_f1 = 0
    
    i = 0
    for correct_sentence in correct_sentences:
        sentence_with_mistakes = introduce_typos_to_text(correct_sentence, typo_chance=0.2) 
        
        corrected_sentence = correct_spelling(sentence_with_mistakes)

        print("Sentence number " + str(i))
        print("  Correct sentence: " + correct_sentence)
        print("  Sentence with mistakes: " + sentence_with_mistakes)
        print("  Corrected sentence: " + corrected_sentence)

        accuracy = calculate_accuracy(correct_sentence, corrected_sentence)
        precision = calculate_precision(correct_sentence, corrected_sentence)
        recall = calculate_recall(correct_sentence, corrected_sentence)
        f1 = calculate_f1(correct_sentence, corrected_sentence)

        summary_accuracy += accuracy
        summary_precision += precision
        summary_recall += recall
        summary_f1 += f1

        print("    Evaluation Results:")
        print("    Accuracy:", accuracy)
        print("    Precision:", precision)
        print("    Recall:", recall)
        print("    F1 Score:", f1)
        
        original_words_list.extend(correct_sentence.split())
        corrected_words_list.extend(corrected_sentence.split())
        i += 1

    
    print("Average Evaluation Results:")
    print("  Accuracy:", summary_accuracy / i)
    print("  Precision:", summary_precision / i)
    print("  Recall:", summary_recall / i)
    print("  F1 Score:", summary_f1 / i)

    

if __name__ == "__main__":
    main()
