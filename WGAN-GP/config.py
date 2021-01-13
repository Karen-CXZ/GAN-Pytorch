import argparse

def parse_arg():

    desc = "Pytorch implementation of WGAN-GP"
    parser=argparse.ArgumentParser(description=desc)

    parser.add_argument('--epochs', type=int, default=200, help="training epochs")
    parser.add_argument('--batch_size', type=int, default=64, help="batch size")
    parser.add_argument('--lr', type=float, default=0.0002, help="adam:learning rate")
    parser.add_argument('--b1', type=float, default=0.5, help="adam: decay of first order momentum of gradient")
    parser.add_argument('--b2', type=float, default=0.999, help="adam: decay of second order momentum of gradient")
    parser.add_argument('--n_cpu', type=int, default=1, help="number of cpu threads during batch generation")
    parser.add_argument('--latent_dim', type=int, default=100, help="dimensionality of the latent space")
    parser.add_argument('--img_size', type=int, default=28, help="image size")
    parser.add_argument('--channels', type=int, default=1, help="number of image channels")
    parser.add_argument('--lameda_gp', type=int, default=10, help="hyper-parameter for gradient penalty")
    parser.add_argument('--n_critic', type=int, default=5, help="the number of training steps for generator per iter")
    parser.add_argument('--sample_interval', type=int, default=500, help="interval between iamge samples")
    parser.add_argument('--checkpoint_interval', type=int, default=10000, help="interval between saving models")
    parser.add_argument('--load_model', type=str, default="checkpoints/generator_done.pth", help="model to load")

    opt = parser.parse_args()
    print(opt)

    return opt