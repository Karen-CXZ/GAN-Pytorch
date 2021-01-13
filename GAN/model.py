import numpy as np
import torch.nn as nn

class Generator(nn.Module):
    def __init__(self, opt):
        super(Generator, self).__init__()

        def block(in_feat, out_feat, normalize=True):
            layers = [nn.Linear(in_feat, out_feat)]
            if normalize:
                layers.append(nn.BatchNorm1d(out_feat, 0.8))
            layers.append(nn.LeakyReLU(0.2, inplace=True))

            return layers

        self.img_shape = (opt.channels, opt.img_size, opt.img_size)
        self.model = nn.Sequential(*block(opt.latent_dim, 128, normalize=False),
                                   *block(128, 256),
                                   *block(256, 512),
                                   *block(512, 1024),
                                   nn.Linear(1024, int(np.prod(self.img_shape))),
                                   nn.Tanh())


    def forward(self, z):
        img = self.model(z)
        print(img)
        img = img.view(img.size(0), *self.img_shape)  #  (batch_size, c, w, h)
        print(img)
        return img

class Discriminator(nn.Module):
    def __init__(self, opt):
        super(Discriminator, self).__init__()

        self.img_shape = (opt.channels, opt.img_size, opt.img_size)
        self.model = nn.Sequential(nn.Linear(int(np.prod(self.img_shape)), 512),
                                   nn.LeakyReLU(0.2, inplace=True),
                                   nn.Linear(512, 256),
                                   nn.Linear(256, 1),
                                   nn.Sigmoid())

    def forward(self, img):
        img_flat = img.view(img.size(0), -1)
        validity = self.model(img_flat)
        return validity

