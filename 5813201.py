import cv2
from skimage import io
from PIL import Image
from matplotlib import pyplot as plt


if __name__ == '__main__':
	print("--------------------------------------")
	print("Hello! It's time to learn the magic of Image Processing.")
	print("Choose one of the number down below, and you will see how it works ><")
	print("1 for JPEG")
	print("2 for PNG")
	print("3 for GIF")
	print("4 for TIFF")
	print("5 for BMP")

	jgray = cv2.imread('jpeg.jpg',0)
	jeqhist = cv2.equalizeHist(jgray)
	
	pgray = cv2.imread("png.png",0)
	peqhist = cv2.equalizeHist(pgray)

	gGray = Image.open('gif.gif').convert('LA')
	gGray.save('greygif.gif')
	gGray = io.imread("greygif.gif", as_gray = True)
	geqhist = cv2.equalizeHist(gGray)

	tgray = cv2.imread("tiff.tiff",0)
	teqhist = cv2.equalizeHist(tgray)

	bgray = cv2.imread("bmp.bmp",0)
	beqhist = cv2.equalizeHist(bgray)

	cv2.imshow("jpeg",jgray)

	while True:
		k = cv2.waitKey(30) & 0xff
		if k==27:
			cv2.destroyAllWindows()
			exit(0) 
		elif k==49:
			plt.figure(figsize=(17, 8))
			plt.subplot(231),plt.imshow(jgray, 'gray'), plt.title("jpeg-grayscale")
			plt.subplot(234),plt.imshow(jeqhist, 'gray'), plt.title("jpeg-grayscale (Equalized)")
			plt.subplot(232),plt.hist(jgray.ravel(),256,[0,256]); plt.title('Histogram for jpeg') 
			plt.subplot(235),plt.hist(jeqhist.ravel(),256,[0,256]); plt.title('Histogram equalization for jpeg') 
			plt.subplot(233),plt.hist(jgray.ravel(),256,[0,256], cumulative = True); plt.title('Cumulative histogram for jpeg') 
			plt.subplot(236),plt.hist(jeqhist.ravel(),256,[0,256], cumulative = True); plt.title('Cumulative histogram equalization for jpeg')
			plt.savefig("jpegGraph.jpg")
			plt.show()
		elif k==50:
			plt.figure(figsize=(17, 8))
			plt.subplot(231),plt.imshow(pgray, 'gray'), plt.title("png-grayscale")
			plt.subplot(234),plt.imshow(peqhist, 'gray'), plt.title("png-grayscale (Equalized)")
			plt.subplot(232),plt.hist(pgray.ravel(),256,[0,256]); plt.title('Histogram for png') 
			plt.subplot(235),plt.hist(peqhist.ravel(),256,[0,256]); plt.title('Histogram equalization for png')
			plt.subplot(233),plt.hist(pgray.ravel(),256,[0,256], cumulative = True); plt.title('Cumulative histogram for png') 
			plt.subplot(236),plt.hist(peqhist.ravel(),256,[0,256], cumulative = True); plt.title('Cumulative histogram equalization for png') 
			plt.savefig("pngGraph.jpg")
			plt.show()
		elif k==51:
			plt.figure(figsize=(17, 8))
			plt.subplot(231),plt.imshow(gGray, 'gray'), plt.title("GIF-grayscale")
			plt.subplot(234),plt.imshow(geqhist, 'gray'), plt.title("GIF-grayscale (Equalized)")
			plt.subplot(232),plt.hist(gGray.ravel(),256,[0,256]); plt.title('Histogram for GIF') 
			plt.subplot(235),plt.hist(geqhist.ravel(),256,[0,256]); plt.title('Histogram equalization for GIF')
			plt.subplot(233),plt.hist(gGray.ravel(),256,[0,256], cumulative = True); plt.title('Cumulative histogram for GIF') 
			plt.subplot(236),plt.hist(geqhist.ravel(),256,[0,256], cumulative = True); plt.title('Cumulative histogram equalization for GIF') 
			plt.savefig("gifGraph.jpg")
			plt.show()
		elif k==52:
			plt.figure(figsize=(17, 8))
			plt.subplot(231),plt.imshow(tgray, 'gray'), plt.title("TIFF-grayscale")
			plt.subplot(234),plt.imshow(teqhist, 'gray'), plt.title("TIFF-grayscale (Equalized)")
			plt.subplot(232),plt.hist(tgray.ravel(),256,[0,256]); plt.title('Histogram for TIFF') 
			plt.subplot(235),plt.hist(teqhist.ravel(),256,[0,256]); plt.title('Histogram equalization for TIFF')
			plt.subplot(233),plt.hist(tgray.ravel(),256,[0,256], cumulative = True); plt.title('Cumulative histogram for TIFF') 
			plt.subplot(236),plt.hist(teqhist.ravel(),256,[0,256], cumulative = True); plt.title('Cumulative histogram equalization for TIFF') 
			plt.savefig("TIFFGraph.jpg")
			plt.show()
		elif k==53:
			plt.figure(figsize=(17, 8))
			plt.subplot(231),plt.imshow(bgray, 'gray'), plt.title("BMP-grayscale")
			plt.subplot(234),plt.imshow(beqhist, 'gray'), plt.title("BMP-grayscale (Equalized)")
			plt.subplot(232),plt.hist(bgray.ravel(),256,[0,256]); plt.title('Histogram for BMP') 
			plt.subplot(235),plt.hist(beqhist.ravel(),256,[0,256]); plt.title('Histogram equalization for BMP')
			plt.subplot(233),plt.hist(bgray.ravel(),256,[0,256], cumulative = True); plt.title('Cumulative histogram for BMP') 
			plt.subplot(236),plt.hist(beqhist.ravel(),256,[0,256], cumulative = True); plt.title('Cumulative histogram equalization for BMP') 
			plt.savefig("BMPGraph.jpg")
			plt.show()