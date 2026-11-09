# Model Card: Mood Machine

This model card is for the Mood Machine project, which includes **two** versions of a mood classifier:

1. A **rule based model** implemented in `mood_analyzer.py`
2. A **machine learning model** implemented in `ml_experiments.py` using scikit learn

You may complete this model card for whichever version you used, or compare both if you explored them.

## 1. Model Overview

**Model type:**  
Describe whether you used the rule based model, the ML model, or both.  
Example: “I used the rule based model only” or “I compared both models.”

I use rule based model first and then try later with ML model after installing it. 

**Intended purpose:**  
What is this model trying to do?  
Example: classify short text messages as moods like positive, negative, neutral, or mixed.

This model is trying to understand user input text messages to classify there mood as postive, negative, neutral, or even mixed. 

**How it works (brief):**  
For the rule based version, describe the scoring rules you created.  
For the ML version, describe how training works at a high level (no math needed).

The rule-based model scores positive and negative words, including negation, emojis, and slang. The ML model learns word patterns from `SAMPLE_POSTS` and `TRUE_LABELS` to predict moods.

## 2. Data

**Dataset description:**  
Summarize how many posts are in `SAMPLE_POSTS` and how you added new ones.

My dataset contains 11 posts currently. What I did I kept the original and just added 5 new post that include sarcasm, salm, mixed feelsing and even including emojis. They also include matching labels.

**Labeling process:**  
Explain how you chose labels for your new examples.  
Mention any posts that were hard to label or could have multiple valid labels.

I label each post based on what I those is mood is. Post that were either postive or neative where mostly easier to label compare to post with sarcasm or unclear language because they might been said in a positive way but was negative or could have more then one mood. 


**Important characteristics of your dataset:**  
Examples you might include:  

- Contains slang or emojis  
- Includes sarcasm  
- Some posts express mixed feelings  
- Contains short or ambiguous messages

The dataset contains slang, emojis, sarcasm, mixed feelings, and short or unclear messages.

**Possible issues with the dataset:**  
Think about imbalance, ambiguity, or missing kinds of language.

The dataset is small, and some labels are subjective. Neutral examples are limited, and the model may not understand new slang or sarcasm.

## 3. How the Rule Based Model Works (if used)

**Your scoring rules:**  
Describe the modeling choices you made.  
Examples:  

- How positive and negative words affect score  
- Negation rules you added  
- Weighted words  
- Emoji handling  
- Threshold decisions for labels

Positve words are worth 1 point add, while negative words subtract 1 point. The model also knows the words after "not", "no" and "never" will have reverse meaning. As for the slang and emojis they are workth stronger scores. A positive score is postive, negative score is negative, zero score is netural, and a positive and negative socore is mixed.

**Strengths of this approach:**  
Where does it behave predictably or reasonably well?

the model works well with clear mood words, simple negation, some common slang, and certain emojis. 

**Weaknesses of this approach:**  
Where does it fail?  
Examples: sarcasm, subtlety, mixed moods, unfamiliar slang.

Its falls in identifying mood with sarcasm, very subytle meanins, slang they never seen before, context clue messages.

## 4. How the ML Model Works (if used)

**Features used:**  
Describe the representation.  
Example: “Bag of words using CountVectorizer.”

**Training data:**  
State that the model trained on `SAMPLE_POSTS` and `TRUE_LABELS`.

**Training behavior:**  
Did you observe changes in accuracy when you added more examples or changed labels?

**Strengths and weaknesses:**  
Strengths might include learning patterns automatically.  
Weaknesses might include overfitting to the training data or picking up spurious cues.

## 5. Evaluation

**How you evaluated the model:**  
Both versions can be evaluated on the labeled posts in `dataset.py`.  
Describe what accuracy you observed.

I tested the rule-based model using the 11 labeled posts in `dataset.py`. It correctly classified 8 out of 11 posts, giving an accuracy of 0.73.

**Examples of correct predictions:**  
Provide 2 or 3 examples and explain why they were correct.

- “I love this class so much” was correctly labeled positive because “love” is a positive word.
- “Today was a terrible day” was correctly labeled negative because “terrible” is a negative word.
- “Feeling tired but kind of hopeful” was correctly labeled mixed because it contains both negative and positive feelings.

**Examples of incorrect predictions:**  
Provide 2 or 3 examples and explain why the model made a mistake.  
If you used both models, show how their failures differed.

- “No, really, I’m totally fine with changing the design for the fifth time today” was labeled neutral, but it was intended to be negative because of sarcasm.
- “Honestly? It’s fine i guess, no big deal.” was labeled neutral, but it was intended to be mixed.
- “Well, that was certainly an event.” was labeled neutral, but it was intended to be mixed because its meaning is unclea

## 6. Limitations

Describe the most important limitations.  
Examples:  

- The dataset is small  
- The model does not generalize to longer posts  
- The model may misclassify sarcasm because it reads emotional words literally and does not understand tone or context  
- It depends heavily on the words you chose or labeled

Curretnly the dataset is small, so it a work in progress especially with the new examples. There is possiblitie that may struggle with longer posts. It is for certain that it's still strugging with sarcasm, unclear langauage and unfamiliar slang words. The model is heavily dependent on the dataset the most.

## 7. Ethical Considerations

Discuss any potential impacts of using mood detection in real applications.  
Examples: 

- Misclassifying a message expressing distress  
- Misinterpreting mood for certain language communities  
- Privacy considerations if analyzing personal messages

It could cause mistakes especially when it misinterprets a message mood incorrectly. Then the person reading the mood detection could get misunderstanding from the message mood identifycation. Also it could invade of privacy.


## 8. Ideas for Improvement

List ways to improve either model.  
Possible directions:  

- Add more labeled data  
- Use TF IDF instead of CountVectorizer  
- Add better preprocessing for emojis or slang  
- Use a small neural network or transformer model  
- Improve the rule based scoring method  
- Add a real test set instead of training accuracy only


Ways I want to improve the model:
- Add more labels to the dataset
- Improve the process mood of the scarasm, slang, emojis, etc.
- I think once fixing all the issues try with real work example like from twitter or just comments on a youtube video. 