import cv2
from skimage import io
from PIL import Image
from matplotlib import pyplot as plt


if __name__ == '__main__':

	###################################################################################
	#introduction to the program 
	print("--------------------------------------")
	print("Hello! It's time to learn the magic of Image Processing.")
	print("Choose one of the number down below, and you will see how it works ><")
	print("1 for JPEG")
	print("2 for PNG")
	print("3 for GIF")
	print("4 for TIFF")
	print("5 for BMP")

	###################################################################################
	#read image from folder 
	jgray = cv2.imread('jpeg.jpg',0)
	#equalize the histogram of the original image
	jeqhist = cv2.equalizeHist(jgray)
	
	pgray = cv2.imread("png.png",0)
	peqhist = cv2.equalizeHist(pgray)

	#OpenCV don't support GIF format	
	#read GIF by 'Image' and convert into grayscale
	gGray = Image.open('gif.gif').convert('LA')
	#save the grayscale image of GIF format to folder
	gGray.save('greygif.gif')
	#read grayscale GIF by 'skimage'
	gGray = io.imread("greygif.gif", as_gray = True)
	geqhist = cv2.equalizeHist(gGray)

	tgray = cv2.imread("tiff.tiff",0)
	teqhist = cv2.equalizeHist(tgray)

	bgray = cv2.imread("bmp.bmp",0)
	beqhist = cv2.equalizeHist(bgray)

	####################################################################################
	#show the image to the user
	cv2.imshow("jpeg",jgray)

	while True:
		#wait for a command from keyboard
		k = cv2.waitKey(30) & 0xff
		
		if k==27: #esc for closing the program
			cv2.destroyAllWindows()
			exit(0) 
		elif k==49: #1 for JPEG
			#configure window size
			plt.figure(figsize=(17, 8))
			#show image
			plt.subplot(231),plt.imshow(jgray, 'gray'), plt.title("jpeg-grayscale")
			plt.subplot(234),plt.imshow(jeqhist, 'gray'), plt.title("jpeg-grayscale (Equalized)")
			#find histogram
			plt.subplot(232),plt.hist(jgray.ravel(),256,[0,256]); plt.title('Histogram for jpeg') 
			plt.subplot(235),plt.hist(jeqhist.ravel(),256,[0,256]); plt.title('Histogram equalization for jpeg') 
			#find cumulative histogram
			plt.subplot(233),plt.hist(jgray.ravel(),256,[0,256], cumulative = True); plt.title('Cumulative histogram for jpeg') 
			plt.subplot(236),plt.hist(jeqhist.ravel(),256,[0,256], cumulative = True); plt.title('Cumulative histogram equalization for jpeg')
			#save all the results to folder
			plt.savefig("jpegGraph.jpg")
			#show all the results
			plt.show()
		elif k==50: #2 for PNG
			plt.figure(figsize=(17, 8))
			plt.subplot(231),plt.imshow(pgray, 'gray'), plt.title("png-grayscale")
			plt.subplot(234),plt.imshow(peqhist, 'gray'), plt.title("png-grayscale (Equalized)")
			plt.subplot(232),plt.hist(pgray.ravel(),256,[0,256]); plt.title('Histogram for png') 
			plt.subplot(235),plt.hist(peqhist.ravel(),256,[0,256]); plt.title('Histogram equalization for png')
			plt.subplot(233),plt.hist(pgray.ravel(),256,[0,256], cumulative = True); plt.title('Cumulative histogram for png') 
			plt.subplot(236),plt.hist(peqhist.ravel(),256,[0,256], cumulative = True); plt.title('Cumulative histogram equalization for png') 
			plt.savefig("pngGraph.jpg")
			plt.show()
		elif k==51: #3 for GIF
			plt.figure(figsize=(17, 8))
			plt.subplot(231),plt.imshow(gGray, 'gray'), plt.title("GIF-grayscale")
			plt.subplot(234),plt.imshow(geqhist, 'gray'), plt.title("GIF-grayscale (Equalized)")
			plt.subplot(232),plt.hist(gGray.ravel(),256,[0,256]); plt.title('Histogram for GIF') 
			plt.subplot(235),plt.hist(geqhist.ravel(),256,[0,256]); plt.title('Histogram equalization for GIF')
			plt.subplot(233),plt.hist(gGray.ravel(),256,[0,256], cumulative = True); plt.title('Cumulative histogram for GIF') 
			plt.subplot(236),plt.hist(geqhist.ravel(),256,[0,256], cumulative = True); plt.title('Cumulative histogram equalization for GIF') 
			plt.savefig("gifGraph.jpg")
			plt.show()
		elif k==52: #4 for TIFF
			plt.figure(figsize=(17, 8))
			plt.subplot(231),plt.imshow(tgray, 'gray'), plt.title("TIFF-grayscale")
			plt.subplot(234),plt.imshow(teqhist, 'gray'), plt.title("TIFF-grayscale (Equalized)")
			plt.subplot(232),plt.hist(tgray.ravel(),256,[0,256]); plt.title('Histogram for TIFF') 
			plt.subplot(235),plt.hist(teqhist.ravel(),256,[0,256]); plt.title('Histogram equalization for TIFF')
			plt.subplot(233),plt.hist(tgray.ravel(),256,[0,256], cumulative = True); plt.title('Cumulative histogram for TIFF') 
			plt.subplot(236),plt.hist(teqhist.ravel(),256,[0,256], cumulative = True); plt.title('Cumulative histogram equalization for TIFF') 
			plt.savefig("TIFFGraph.jpg")
			plt.show()
		elif k==53: #5 for BMP
			plt.figure(figsize=(17, 8))
			plt.subplot(231),plt.imshow(bgray, 'gray'), plt.title("BMP-grayscale")
			plt.subplot(234),plt.imshow(beqhist, 'gray'), plt.title("BMP-grayscale (Equalized)")
			plt.subplot(232),plt.hist(bgray.ravel(),256,[0,256]); plt.title('Histogram for BMP') 
			plt.subplot(235),plt.hist(beqhist.ravel(),256,[0,256]); plt.title('Histogram equalization for BMP')
			plt.subplot(233),plt.hist(bgray.ravel(),256,[0,256], cumulative = True); plt.title('Cumulative histogram for BMP') 
			plt.subplot(236),plt.hist(beqhist.ravel(),256,[0,256], cumulative = True); plt.title('Cumulative histogram equalization for BMP') 
			plt.savefig("BMPGraph.jpg")
			plt.show()