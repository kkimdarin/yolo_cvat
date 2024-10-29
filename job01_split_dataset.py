import os
import random
import shutil

def split_dataset(output_dir, train_ratio, val_ratio):
    assert train_ratio + val_ratio == 1.0

    images_dir = os.path.join('images')
    labels_dir = os.path.join('labels')

    subsets = ['train', 'val']
    for subset in subsets:
        os.makedirs(os.path.join(output_dir, 'images', subset), exist_ok=True)
        os.makedirs(os.path.join(output_dir, 'labels', subset), exist_ok=True)

    image_files = os.listdir(images_dir)
    random.shuffle(image_files)

    train_size = int(len(image_files) * train_ratio)
    val_size = int(len(image_files) * val_ratio)

    train_images = image_files[:train_size]
    val_images = image_files[train_size:train_size+val_size]

    for subset, subset_images in [('train', train_images), ('val', val_images)]:
        for image_file in subset_images:
            image_path = os.path.join(images_dir, image_file)
            label_file = os.path.splitext(image_file)[0] + '.txt'
            label_path = os.path.join(labels_dir, label_file)

            shutil.copy(image_path, os.path.join(output_dir, 'images', subset))
            shutil.copy(label_path, os.path.join(output_dir, 'labels', subset))

    print(f"{output_dir} 폴더가 생성됐습니다.")

if __name__ == "__main__":
    #dataset_dir = r'.\dataset'
    output_dir = 'dataset'
    train_ratio = 0.8
    val_ratio = 0.2

    split_dataset(output_dir, train_ratio, val_ratio)