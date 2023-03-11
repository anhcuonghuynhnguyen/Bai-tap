from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import precision_recall_fscore_support
from sklearn.model_selection import cross_val_score
import numpy as np

# Load data
newsgroups_train = fetch_20newsgroups(subset='train')
newsgroups_test = fetch_20newsgroups(subset='test')

# Vectorize text data
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
X_train_tfidf = tfidf_vectorizer.fit_transform(newsgroups_train.data)
X_test_tfidf = tfidf_vectorizer.transform(newsgroups_test.data)

# Train classifier
classifier_tfidf = MultinomialNB()
classifier_tfidf.fit(X_train_tfidf, newsgroups_train.target)

# Test classifier
y_pred_tfidf = classifier_tfidf.predict(X_test_tfidf)

# Evaluate performance
precision_tfidf, recall_tfidf, fscore_tfidf, support_tfidf = precision_recall_fscore_support(
    newsgroups_test.target, y_pred_tfidf, average='macro')

print('Precision (TF-IDF):', precision_tfidf)
print('Recall (TF-IDF):', recall_tfidf)
print('F1-score (TF-IDF):', fscore_tfidf)

# Cross-validation
scores = cross_val_score(classifier_tfidf, X_train_tfidf,
                         newsgroups_train.target, cv=5)

print('Cross-validation scores:', scores)
print('Mean score:', np.mean(scores))
