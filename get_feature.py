import json
def read_file_flick(path):
  file = open(path,'r')
  data = file.read()
  data = data.split('\n')
  result = {}
  for row in data:
    if row != '':
      column = row.split('\t')
      string = column[0][:-2]
      if string[-3:] == 'jpg':
        caption = column[1]
        if string in result.keys():
          result[string].append(caption.strip())
        else:
          result[string] = [caption.strip()]
  return result
def read_train_file(path):
  file = open(path,'r')
  data = file.read()
  return data.split('\n')
def get_train_caption(main,train):
  result = {}
  for filename in train:
    if filename != '':
      result[filename] = main[filename]
  return result

main_file = read_file_flick('/content/Flickr8k.token.txt')
train_file = read_train_file('/content/Flickr_8k.trainImages.txt')
img_caption_file = get_train_caption(main_file,train_file)
with open('/content/transformer-image-captioning/source/caption.json', 'w') as json_file:
  json.dump(img_caption_file, json_file)
  
python main.py processing --path2captions /content/transformer-image-captioning/source/caption.json \
            --path2images /content/transformer-image-captioning/images \
            --path2vectorizer /content/transformer-image-captioning/models/resnet152.th \
            --extension jpg \
            --path2features /content/transformer-image-captioning/target/map_img2features.pkl \
            --path2tokenids /content/transformer-image-captioning/target/zip_img2tokenids.pkl \
            --path2vocabulary /content/transformer-image-captioning/target/vocabulary.pkl