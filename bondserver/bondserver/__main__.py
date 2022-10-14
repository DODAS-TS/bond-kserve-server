import argparse

import kserve
from bondserver import BondModel

parser = argparse.ArgumentParser(parents=[kserve.model_server.parser])
parser.add_argument('--model_uri', required=True,
                    help='A URI pointer to the model binary')
parser.add_argument('--model_name', default='custom-model',
                    help='The name that the model is served under.')
args, _ = parser.parse_known_args()

if __name__ == "__main__":
    model = BondModel(args.model_name, args.model_uri)
    model.load()
    kserve.ModelServer(workers=1).start([model])
