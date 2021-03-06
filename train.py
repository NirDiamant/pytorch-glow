import sys
import signal
import argparse

from torchvision import transforms

from misc import util
from network import Builder, Trainer
from dataset import CelebA


# def parse_args():
#     parser = argparse.ArgumentParser(
#         description='PyTorch implementation of "Glow: Generative Flow with Invertible 1x1 Convolutions"')
#     parser.add_argument('profile', type=str,
#                         default='profile/celeba.json',
#                         help='path to profile file')
#     return parser.parse_args()


if __name__ == '__main__':
    # this enables a Ctrl-C without triggering errors
    signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))
    print("hello")
    # parse arguments
    #args = parse_args()
    args = "profile/celeba.json"
    # initialize logging
    util.init_output_logging()

    # load hyper-parameters
    # hps = util.load_profile(args.profile)
    hps = util.load_profile(args)
    util.manual_seed(hps.ablation.seed)

    # build graph
    builder = Builder(hps)
    state = builder.build()

    # load dataset
    dataset = CelebA(root=hps.dataset.root,
                     transform=transforms.Compose((
                         transforms.CenterCrop(160),
                         transforms.Resize(128),
                         transforms.ToTensor()
                     )))

    # start training
    trainer = Trainer(hps=hps, dataset=dataset, **state)
    trainer.train()
