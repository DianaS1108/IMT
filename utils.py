import torch
from torch import nn
from torch.utils.data import Dataset


# Cast data to dataset
class CastedDataset(Dataset):

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
    
    def __len__(self):
        return len(self.y)
    
    def __getitem__(self, idx):
        return self.x[idx], self.y[idx]


# Logistic regression model
class LogisticRegression(nn.Module):
    
    def __init__(self, in_dim=2):
        super().__init__()
        self.linear = nn.Linear(in_dim, 1)
    
    def forward(self, x):
        x = x.reshape(-1, x.shape[-1])  # (batch_size, x_dim)
        return self.linear(x).squeeze(1)  # (batch_size)


# Training log tool
class Log():
    def __init__(self):
        self.iter = 0
        self.w_dist = []
        self.train_loss = []
        self.test_acc = []
