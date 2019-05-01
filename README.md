This repository contains codes related to navigating a robot. The aim is to collect yellow bananas in the environment and avoid the blue bananas.

In order to use the repository, follow the steps:
1. git clone https://github.com/Santosh-16k/Udacity_DRL_NanoDegree_p1.git
2. Get the Unity environment from the following link and paste it in the repo:
    [Linux](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip)
    [Mac OSX](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
    [Windows (32-bit)](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
    [Windows (64-bit)](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)
3. Navigation.ipynb is the main notebook that you can use to train your model or use load the trained model and see how it works.
4. DQN_agent.py contains code elements needed for the agent like experience replay, taking action in the environment, etc.
5. model.py contains the neural network model architecture that is used to train the agent and inference from the trained one.
6. checkpoint.pth contains trained model, use the notebook to load the model.
