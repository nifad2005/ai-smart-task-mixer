import random
from database import task_list
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder

def shuffle_tasks(task_list):
    random.shuffle(task_list)
    return task_list

def personalize_task_order(task_list,mood,energy):
    new_order = []
    for task in task_list:
        if task['mood'] == mood and task['energy'] == energy:
            new_order.append(task)
    return new_order


def handle_data_preparation_and_vectorization(csv_data_to_train_model):
    # Data processing
    csv_data_to_train_model.dropna(inplace=True)
    csv_data_to_train_model = csv_data_to_train_model.applymap(lambda x: x.lower() if isinstance(x, str) else x)
    csv_data_to_train_model['text'] = csv_data_to_train_model['text']+csv_data_to_train_model['text2']
    mood_X_train,mood_X_test,mood_y_train,mood_y_test = train_test_split(csv_data_to_train_model['text'],csv_data_to_train_model['mood'])
    energy_X_train,energy_X_test,energy_y_train,energy_y_test = train_test_split(csv_data_to_train_model['text'],csv_data_to_train_model['energy'],test_size=0.2,random_state=42,shuffle=True)



    # Features Vectorizing
    vectorizer = TfidfVectorizer()
    vectorizer.fit_transform(csv_data_to_train_model['text'])
    mood_X_train = vectorizer.transform(mood_X_train)
    mood_X_test = vectorizer.transform(mood_X_test)
    energy_X_train = vectorizer.transform(energy_X_train)
    energy_X_test = vectorizer.transform(energy_X_test)

    # Label Encoding
    mood_label_encoder = LabelEncoder()
    energy_label_encoder = LabelEncoder()
    mood_y_train = mood_label_encoder.fit_transform(mood_y_train)
    energy_y_train = energy_label_encoder.fit_transform(energy_y_train)
    mood_y_test = mood_label_encoder.transform(mood_y_test)
    energy_y_test = energy_label_encoder.transform(energy_y_test)

    mood_model_train(mood_X_train,mood_y_train,mood_X_test,mood_y_test,vectorizer,mood_label_encoder)
def mood_model_train(mood_X_train,mood_y_train,mood_X_test,mood_y_test,vectorizer,mood_label_encoder):
    mood_naive_bayes_model = MultinomialNB()
    mood_naive_bayes_model.fit(mood_X_train,mood_y_train)
    mood_predictions = mood_naive_bayes_model.predict(mood_X_test)
    mood_accuracy = accuracy_score(mood_y_test,mood_predictions)
    print(f"Mood Accuracy: {round(mood_accuracy*100,2)}%")
    
    text_input = input("Express your mood : ").lower()
    text_input = vectorizer.transform([text_input])
    predicted_mood = mood_label_encoder.inverse_transform(mood_naive_bayes_model.predict(text_input))
    print(f"Predicted Mood: {predicted_mood[0]}")






   

def handle_whole_ml_workflow():
    csv_data_to_train_model = pd.read_csv('./smart-task-mixer/dataset.csv')
    handle_data_preparation_and_vectorization(csv_data_to_train_model)
    






def main():
    # organized_tasks = shuffle_tasks(task_list)
    organized_tasks = personalize_task_order(task_list,'Creative','Medium')
    handle_whole_ml_workflow()


    count = 1
    show = False
    if show :
        for task in organized_tasks:
            print(f"Task {count}: {task['title']}")
            count += 1






if __name__ == '__main__':
    main()