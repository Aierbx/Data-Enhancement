import os
import xml.etree.ElementTree as ET

size_h = []
size_w = []


def get_xml_in(path):
    box = []
    n = []
    tree = ET.parse(path)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    size_h.append(h)
    size_w.append(w)
    print('图像宽度为：', w, '，高度为：', h)

    for obj in root.iter('object'):
        xmlbox = obj.find('bndbox')
        xmlname = obj.find('name')
        b = [float(xmlbox.find('xmin').text), float(xmlbox.find('ymin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymax').text)]
        box.append(b)
        n.append(xmlname.text)
    return box, n

def create_txt_file(file_path, image_path, i, bboxes, class_names, m):
    f = open(file_path + '/' + image_path + str(i) + 'crop-' + str(m) + '.txt', 'w')
    i -= 1
    w = size_w[i]
    h = size_h[i]
    dw = 1. / w
    dh = 1. / h

    for t in class_names:
        bbox = bboxes[t]
        class_name = class_names[t]
        x = (bbox[0] + bbox[2]) / 2.0
        y = (bbox[1] + bbox[3]) / 2.0
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        x = str(x * dw)
        w = str(w * dw)
        y = str(y * dh)
        h = str(h * dh)
        yolo_txt = [str(class_name), x, y, w, h]
        yolo_txt = ' '.join(yolo_txt)
        f.write(yolo_txt)
    f.close()

def read_xml(in_file_dir):
    xml_file_dir = []
    bboxes = []
    category_ids = []
    for variety in os.listdir(in_file_dir):
        file_path = in_file_dir + variety
        for xml_path in os.listdir(file_path):
            if '.jpg' in xml_path:
                continue
            path = file_path + '/' + xml_path
            xml_file_dir.append(path)

            box, category = get_xml_in(path)

            bboxes.append(box)
            category_ids.append(category)

    return bboxes, category_ids