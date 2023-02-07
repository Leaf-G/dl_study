import torch

a = torch.arange(12)
b =a.reshape((3,4))
b[:] = 2
print(a , b)