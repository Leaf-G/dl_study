import torch

x=torch.arange(4.0)
print(x)

x.requires_grad_(True)
print(x.grad)

y=2*torch.dot(x,x)
print(y)

y.backward()
print(x.grad)

x.grad.zero_()#梯度清零
y=x.sum()
y.backward()
print(x.grad)