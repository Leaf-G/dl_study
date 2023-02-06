import torch

x=torch.arange(12)

y=x.numel()

x=x.reshape(3,4)
print(x)
print(y)