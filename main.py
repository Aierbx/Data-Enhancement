import cv2
import os
import albumentations as A
import Visualize
import Getfile



in_file_dir = 'E:/Users/Administrator/Desktop/data/image cropping/crop/'                       #原图像路径
classes = ['class1', 'class2']                                                                 #类别名称
category_id_to_name = {'class-1': '1', 'class-2': '2'}                                         #类别与编号对应的字典
image_file_dir = 'E:/Users/Administrator/Desktop/data/image cropping/new_path/image_new'       #增强后的图像存储路径

BOX_COLOR = (255, 0, 0)                                                                        #边界框颜色，此处为RED
TEXT_COLOR = (255, 255, 255)                                                                   #图像中文字颜色，此处为WHITE

bboxes, category_ids = Getfile.read_xml(in_file_dir)
i = 0
for variety in os.listdir(in_file_dir):

    file_path = in_file_dir + variety
    m = 0
    for image_name in os .listdir(file_path):

        cropped = 0
        if i >= len(bboxes):
            break
        bbox = bboxes[i]
        bcategory = category_ids[i]
        if '.jpg' not in image_name:
            continue
        image_path = file_path + '/' + image_name
        pre_image = cv2.imread(image_path)
        image = cv2.cvtColor(pre_image, cv2.COLOR_BGR2RGB)
        for w in range(len(bbox)):
            Visualize.Visualize(image, bbox, bcategory, category_id_to_name, cropped, image_name, i+1, m, image_file_dir)
        image_path.replace('.jpg', '--')
        cropped += 1
        for m in range(10):
            transform = A.Compose([
                A.OneOf([
                    A.HorizontalFlip(),
                    A.Transpose(),
                    A.RandomRotate90(),
                    A.ShiftScaleRotate()
                ]),
                A.OneOf([
                    A.HorizontalFlip(),
                    A.Transpose(),
                    A.RandomRotate90(),
                    A.ShiftScaleRotate()
                ]),
                A.OneOf([
                    A.HorizontalFlip(),
                    A.Transpose(),
                    A.RandomRotate90(),
                    A.ShiftScaleRotate()
                ])
            ],
                bbox_params=A.BboxParams(format='pascal_voc', label_fields=['category_ids'])
            )
            transformed = transform(image=image, bboxes=bbox, category_ids=bcategory)
            transformed['bboxes'] = list(transformed['bboxes'])
            Visualize.Visualize(
                transformed['image'],
                transformed['bboxes'],
                transformed['category_ids'],
                category_id_to_name,
                cropped,
                image_name,
                i + 1,
                m,
                image_file_dir
            )

            print('第'+ str(i+1) +'个图像的第' + str(m+1) + '次增强完毕')
            class_name = []
            for t in range(len(classes)):
                for o in range(len(transformed['category_ids'])):
                    if classes[t] == transformed['category_ids'][o]:
                        class_name.append(t)
                    else:
                        continue
            image_name = image_name.replace('.jpg', '')
            Getfile.create_txt_file(image_file_dir, image_name, i+1, transformed['bboxes'], class_name, m)

        i += 1

