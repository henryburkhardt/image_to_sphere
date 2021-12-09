# image_to_sphere
Rendering 2d images into 3d environments of spheres in Unity using Python. Images are halftoned using a python program I built, then data about the location and radius of every circle is stored in a CSC files. Next, a C# program I built reads the CSV file and creates spheres in a 3d enviroment where the Z axis position is defined realtive to the size of any given sphere. 

Here's an example of rendering a black and white image of a face into a 3d enviroment:

https://www.youtube.com/watch?v=JmCNsPvIqq4
