import torch
from torch import nn
import torch.nn.functional as F

class QNet(nn.Module):
    def __init__(self, state_size, action_size, seed):
        self.action_size = action_size
        self.state_size = state_size
        super(QNet,self).__init__()
        self.seed = torch.manual_seed(seed)

        self.fc1 = nn.Linear(self.state_size, 256)
        self.fc2 = nn.Linear(256, 128)
        self.fc3 = nn.Linear(128, self.action_size)

    def forward(self, state):
        x = F.relu(self.fc1(state))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)

        return x