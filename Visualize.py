import cv2
import matplotlib.pyplot as plt

BOX_COLOR = (255, 0, 0)
TEXT_COLOR = (255, 255, 255)

def Visualize_bbox(img, bbox, class_name, color=BOX_COLOR, thickness=2):
    x_min, y_min, x_max, y_max = bbox

    x_min, x_max, y_min, y_max = int(x_min), int(x_max), int(y_min), int(y_max)

    cv2.rectangle(img, (x_min, y_min), (x_max, y_max), color=color, thickness=thickness)
    ((text_width, text_height), _) = cv2.getTextSize(class_name, cv2.FONT_HERSHEY_SIMPLEX, 0.35, 1)
    cv2.rectangle(img, (x_min, y_min - int(1.3 * text_height)), (x_min + text_width, y_min), BOX_COLOR, -1)
    cv2.putText(
        img,
        text=class_name,
        org=(x_min, y_min - int(1.3 * text_height)),
        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=0.35,
        color=TEXT_COLOR,
        lineType=cv2.LINE_AA
    )
    return img


def Visualize(image, bboxes, category_ids, category_id_to_name, cropped, image_path, i, m, save_dir = None, color = BOX_COLOR, thickness = 2):
    img = image.copy()
    for bbox, category_id in zip(bboxes, category_ids):

        class_name = category_id_to_name.get(category_id)
        if cropped:
            plt.figure(figsize=(12, 12))
            plt.axis('off')
            plt.imshow(img)
            image_path = image_path.replace('.jpg', '')
            plt.savefig(save_dir + '/' + image_path + str(i) + 'crop-' + str(m) + '.jpg')
        else:
            img = Visualize_bbox(img, bbox, class_name, color, thickness)
            plt.figure(figsize=(12, 12))
            plt.axis('off')
            plt.imshow(img)
            plt.show()


if __name__ == '__main__':
    print('Done!')
