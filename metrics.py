from sklearn.metrics import precision_score, recall_score, f1_score

def calculate_accuracy(y_true, y_pred):
    if len(y_true) == 0:  
        return 0.0
    correct_predictions = sum(1 for true, pred in zip(y_true, y_pred) if true == pred)
    return correct_predictions / len(y_true)

def calculate_precision(y_true, y_pred):
    true_positive = sum(1 for true, pred in zip(y_true, y_pred) if true == pred and true != "")
    false_positive = sum(1 for pred in y_pred if pred != "" and pred not in y_true)
    
    if true_positive + false_positive == 0:  
        return 0.0
    return true_positive / (true_positive + false_positive)

def calculate_recall(y_true, y_pred):
    true_positive = sum(1 for true, pred in zip(y_true, y_pred) if true == pred and true != "")
    false_negative = sum(1 for true in y_true if true != "" and true not in y_pred)
    
    if true_positive + false_negative == 0:  
        return 0.0
    return true_positive / (true_positive + false_negative)

def calculate_f1(y_true, y_pred):
    precision = calculate_precision(y_true, y_pred)
    recall = calculate_recall(y_true, y_pred)
    
    if precision + recall == 0:  
        return 0.0
    return 2 * (precision * recall) / (precision + recall)
