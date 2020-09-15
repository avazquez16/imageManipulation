######################################################
# Project: Image Manipulation 


from PIL import Image
import random


# class - accpets an Image object and makes a copy as an instance variable
class ImageSpecial:
  def __init__(self, image):
    self.image = image.copy()



  # method that accepts an rgb tuple and sets transparent pixels to the parameter value
  def set_background(self,color):
    h, w = self.image.size
    for x in range(w):
      for y in range(h):
        r,g,b,a = self.image.getpixel((x,y))
        if a == 0:
          new_color = (color[0],color[1],color[2], 255)
          self.image.putpixel((x,y), new_color)



  # method that  accepts a color name ("red", "green" or "blue") and sets that color value to 0 for all pixels
  def remove_color(self,color_name):
    h, w = self.image.size
    for x in range(w):
      for y in range(h):
        r,g,b,a = self.image.getpixel((x,y))
        if color_name == "red":
          new_color = (0,g,b,a)
        elif color_name == "green":
          new_color = (r,0,b,a)
        elif color_name == "blue":
          new_color = (r,g,0,a) 
        self.image.putpixel((x,y), new_color)


    # method that  accepts a color name ("red", "green" or "blue") and sets that color value to HALF for all pixels
  def remove_half_color_value(self,color_name):
    h, w = self.image.size
    for x in range(w):
      for y in range(h):
        r,g,b,a = self.image.getpixel((x,y))
        if color_name == "red":
          new_color = (int(r/2),g,b,a)
        elif color_name == "green":
          new_color = (r,int(g/2),b,a)
        elif color_name == "blue":
          new_color = (r,g,int(b/2),a) 
        self.image.putpixel((x,y), new_color)


  # method mirrors image horizontal
  def mirror_horizontal(self):
    h, w = self.image.size
    for x in range(int(w/2)):
      for y in range(int(h)):
        r,g,b,a = self.image.getpixel((x,y))
        mirror_x = w- x -1
        self.image.putpixel((mirror_x,y), (r,g,b,a))

    



# method in which the class and methods in that class are called to manipulate the original image and make a collage   

def main():


  # opening original image
  img = Image.open("Gold_Dropsy.png")


  # choosing a random int for the number of rows and columns
  row_int = random.randint(1,5)
  col_int = random.randint(2,5)
 
  


  # asking for size of image to make to make a  grid of that image 
  image_heigth = 300
  image_width = 300
  

  # creating the new image were the modified images will be pasted
  collage = Image.new(img.mode,(col_int * image_width, row_int * image_heigth))
 


  # pasting original image at 0,0 position  by using a boolean and creating a nested for loop through the pixels and pasting a modified image that fits the collage
  counter = True
  for row in range(row_int ):
    for col in range(col_int ):
      collage_img = ImageSpecial(img)
      if counter == True:      
        collage.paste(collage_img.image, (0, 0))
        counter = False
        continue 

        

      #6 modification options that will randomly be choseen
      mod_num = random.randint(0,5)


      # mod will remove all RED pixels and set the background to transparent pixels with parameter (Random.randint(0,255),255,255)
      if mod_num == 0:
        collage_img.set_background((random.randint(0,255),255,255))
        collage_img.remove_color("red")
        paste_x = col * image_width
        paste_y = row * image_heigth
        collage.paste(collage_img.image, (paste_x, paste_y ))

      # mod will remove all BLUE pixels and set the background to transparent pixels with parameter (255,random.randint(0,120,255)
      elif mod_num == 1:  
        collage_img.set_background((255,random.randint(0,120),255))
        collage_img.remove_color("blue")
        paste_x = col * image_width
        paste_y = row * image_heigth
        collage.paste(collage_img.image, (paste_x, paste_y ))

      #  mod will remove all GREEN pixels and set the background to transparent pixels with parameter (random.randint(0,255),random.randint(0,255),random.randint(0,255)
      elif mod_num == 2:
        collage_img.set_background((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        collage_img. remove_color("green")
        paste_x = col * image_width
        paste_y = row * image_heigth
        collage.paste(collage_img.image, (paste_x, paste_y ))

      # mod will remove half the RED pixels and rotate dandom angle from 1-360
      elif mod_num == 3:
        collage_img.image = collage_img.image.rotate(random.randint(1,360) )
        collage_img.remove_half_color_value("red")
        paste_x = col * image_width
        paste_y = row * image_heigth
        collage.paste(collage_img.image, (paste_x, paste_y ))

      #mod will set the background to transparent pixels with parameter (255,random.randint(0,255),0), remove all GREEN pixels, will remove half of the BLUE value and rotate image 270 degrees
      elif mod_num == 4:
        collage_img.image = collage_img.image.rotate( 270 )
        collage_img.set_background((255,random.randint(0,255),0))
        collage_img.remove_color("green")
        collage_img.remove_half_color_value("blue")
        collage_img.image = collage_img.image.rotate( 270 )
        paste_x = col * image_width
        paste_y = row * image_heigth
        collage.paste(collage_img.image, (paste_x, paste_y ))

      # mod rotates random angel from 1-360 removes GREEN pixels and mirrors image horizontal 
      elif mod_num == 5:
        collage_img.mirror_horizontal()    
        collage_img.image = collage_img.image.rotate( random.randint(1,360) )
        collage_img.remove_color("blue")
        paste_x = col * image_width
        paste_y = row * image_heigth
        collage.paste(collage_img.image, (paste_x, paste_y ))
    
    
    
  collage.save("collage.png")    


main()

         
  