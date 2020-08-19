# sign-language-detection
## This app automatically detects the American Sign Language using Deep Learning
This is the code for Sign Language Detection.
1. Run app.py, an UI will appear.
2. Click on "webcam" button at the end of page.
3. Web-Cam will open, do the appropriate gesture and ouput is shown parallely.

## Data Collection
Data is avialable on kaggle https://www.kaggle.com/datamunge/sign-language-mnist

## Code Structure
1. model_building.py contains code to build the Deep Learning model. Here, we used CNN to build model using Keras.
2. After model completion, it is saved in CNNmodel.h5 file.
3. app.py contains front end, it captures user's gesture and pass it to the model for prediction.
