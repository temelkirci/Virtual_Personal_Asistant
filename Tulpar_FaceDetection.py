import cv2
import numpy as np

from imutils.video import FPS

class Tulpar_FaceDetection:
    def __init__(self):
        self.video_path = r"C:/Users/temel/Desktop/feel/Married Pussy Feels So Good - XVIDEOS.COM.ts"

        #self.FrameCapture(self.video_path)

    def FrameCapture(self, path):
        cap = cv2.VideoCapture(path)
        #cap.set(cv2.CAP_PROP_POS_MSEC, 20000)  # just cue to 20 sec. position

        print("started")
        i = 0
        last_index = 0

        while (cap.isOpened()):
            ret, frame = cap.read()
            if ret == False:
                break

            if (i != 0) and (i % 1000 == 0):
                cv2.imwrite('C:/Users/temel/Desktop/Tulpar/Virtual_Personal_Asistant/output/xxx' + str(i) + '.jpg', frame)
                print("xxx"+ str(i) + " added")
                last_index = i
            i += 1

        # read image
        img = cv2.imread('C:/Users/temel/Desktop/Tulpar/Virtual_Personal_Asistant/output/xxx'+ str(last_index) +".jpg", cv2.IMREAD_UNCHANGED)

        # get dimensions of image
        dimensions = img.shape

        # height, width, number of channels in image
        height = img.shape[0]
        width = img.shape[1]
        channels = img.shape[2]

        print('Image Dimension    : ', dimensions)
        print('Image Height       : ', height)
        print('Image Width        : ', width)
        print('Number of Channels : ', channels)

        cap.release()
        cv2.destroyAllWindows()


    def Init(self):
        # initialize the HOG descriptor/person detector
        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

        cv2.startWindowThread()
        cap = cv2.VideoCapture(0)

        # the output will be written to output.avi
        out = cv2.VideoWriter(
            'Records/output.avi',
            cv2.VideoWriter_fourcc(*'MJPG'),
            15.,
            (640, 480))

        #mixer.init()
        #mixer.music.load('Sounds/alarm.mp3')

        fps = FPS().start()

        while (True):
            # Capture frame-by-frame
            ret, frame = cap.read()

            # resizing for faster detection
            frame = cv2.resize(frame, (640, 480))
            # using a greyscale picture, also for faster detection
            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

            # detect people in the image
            # returns the bounding boxes for the detected objects
            boxes, weights = hog.detectMultiScale(frame, winStride=(8, 8))

            boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

            for (xA, yA, xB, yB) in boxes:
                # display the detected boxes in the colour picture
                cv2.rectangle(frame, (xA, yA), (xB, yB),
                              (0, 255, 0), 2)

            # Write the output video
            out.write(frame.astype('uint8'))
            # Display the resulting frame
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                #mixer.music.play(0)
                break
            fps.update()

        fps.stop()
        print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
        print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

        # When everything done, release the capture
        cap.release()
        # and release the output
        out.release()
        # finally, close the window
        cv2.destroyAllWindows()
        cv2.waitKey(1)