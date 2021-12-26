import argparse
from tflite_model_maker import image_classifier
from tflite_model_maker.image_classifier import DataLoader


def train_model(data_dir, export_dir):

    data = DataLoader.from_folder(data_dir)
    model = image_classifier.create(data)

    loss, accuracy = model.evaluate(data)
    model.export(export_dir=export_dir)


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--train_dir', type=str, help='path to the train dataset')
    parser.add_argument('--export_dir', type=str, help='path to the folder where save model')
    
    args, _ = parser.parse_known_args()
    train_model(args.train_dir, args.export_dir)
