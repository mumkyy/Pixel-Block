from PIL import Image
import csv

# Image Grid Function taken from this Stack Overflow thread :
# https://stackoverflow.com/questions/37921295/python-pil-image-make-3x3-grid-from-sequence-images
def image_grid(imgs, rows, cols):
    assert len(imgs) == rows*cols

    w, h = imgs[0].size
    grid = Image.new('RGB', size=(cols*w, rows*h))
    grid_w, grid_h = grid.size
    
    for i, img in enumerate(imgs):
        grid.paste(img, box=(i%cols*w, i//cols*h))
    return grid


# generates a final image of all the blocks put together and stuff
def stitch(data,size):
    images = []
    with open(data) as data:
        dreader = csv.reader(data)
        rows = list(dreader)
    rows.pop(0)
    for x in rows:
        img = Image.open('block/' + x[0] + '.png')
        images.append(img.copy())
        img.close()
    image = image_grid(images,size[1],size[0])
    image = image.save('final.png')

