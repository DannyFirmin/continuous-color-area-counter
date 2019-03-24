# continuous-color-area-counter
Count number of coloured areas in an image

My friend Kalai and I will contribute to this repo together and improve the solution. Welcome anybody to join and improve or even develop a better AI algorithm to solve this.

Write a clean, readable, maintainable, and reasonably memory- and CPU-efficient program to count number of coloured areas in an image.
 

Input: a grey-scale image represented as a 2-dimensional array of unsigned bytes.

Output: array of 256 unsigned int numbers, each of them being a count of areas coloured with the corresponding shade of grey.


For example, if a image has 2 white areas, 3 black areas, and 2 grey areas (with value 200), i.e. the output array A will have all its elements set to 0, except A[0] that will be set to 3, A[255] will be 2, and A[200] will be 2.

 
The implementation are in Python. Run the code as following, with text output on stdout:

python count-areas.py <input-filename>

Where input file is a binary representation of 2D unsigned char array and the output to stdout is 256 numbers corresponding to the area counts for pixel values 0, 1, ..., 255
