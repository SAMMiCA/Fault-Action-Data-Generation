import argparse


def get_args():
    parser = argparse.ArgumentParser(description='Dataset')
    # Arguments
    parser.add_argument('--target-action', default='movement', type=str,
                        choices=['movement',
                                 'crouch',
                                 'pickup'],
                        help='target action')
    parser.add_argument('--target-state', default='normal', type=str,
                        choices=['normal',
                                 'fault'],
                        help='target state')
    parser.add_argument('--max-data-num', type=int, default=1000, help='max data number')
    parser.add_argument('--save-root', type=str, default='./dataset/', help='save root')

    parser.add_argument('--fov', type=int, default=90, help='FOV of robot')
    
    parser.add_argument('--move-mag', type=float, default=0.25, help='target magnitude of movement')
    parser.add_argument('--rotate-deg', type=int, default=45, help='target degree of rotation')
    parser.add_argument('--move-fault-dist', type=float, default=0.03, help='mininum fault distance of movement')
    parser.add_argument('--move-fault-dist-rate', type=float, default=0.12, help='minimum fault distance rate of movement')
    parser.add_argument('--rotate-fault-deg', type=int, default=5, help='mininum fault degree of rotation')
    parser.add_argument('--rotate-fault-deg-rate', type=float, default=1/9, help='mininum fault degree rate of rotation')

    parser.add_argument('--max-pickup-dist', type=float, default=1.0, help='max distance of pickup')

    args=parser.parse_args()
    return args

