from display import DisplayManager
from threading import Thread
from settings import *
from gestureflow.tracker import HandTracker
from gestureflow.sample_gesture_trackers import GestureTracker2D
from gestureflow.sample_state_trackers import RotationCounter, PositionTracker
from gestureflow.sample_runners import Runner
from gestureflow.definitions import *
from state_trackers import *

SLIDE_CHANGE_GESTURE = [True, True, False, False, True]
SLIDE_CHANGE_GESTURE = [True, True, True, False, False]
POINTER_GESTURE = [False, True, False, False, False]
ANNOTATION_GESTURE = [False, True, True, False, False]
ERASER_GESTURE = [True, True, True, True, True]


if __name__ == "__main__":
    state = DEFAULT_STATE_DICT

    handTracker = HandTracker()

    gesture1 = GestureTracker2D()
    gesture2 = GestureTracker2D()
    gesture3 = GestureTracker2D()
    gesture4 = GestureTracker2D()

    displayManager = DisplayManager()

    slideNumber = RotationCounter()
    pointer = PositionTracker()
    annotation = AnnotationTracker(displayManager)
    eraser = EraserTracker(displayManager)

    runner = Runner()

    slideNumber.setMin(0)
    slideNumber.setMax(10)
    slideNumber.setDiscUnit(30)

    def set_slide_number(slideNo):
        slideNo = int(slideNo)
        displayManager.setSlideNumber(slideNo)

    def show_pointer(coords):
        displayManager.show_pointer(coords[1])

    def annotate(coords):
        displayManager.annotate(coords[1])

    gesture1.addGesture(SLIDE_CHANGE_GESTURE)
    gesture2.addGesture(POINTER_GESTURE)
    gesture3.addGesture(ANNOTATION_GESTURE)
    gesture4.addGesture(ERASER_GESTURE)

    gesture1.addStateTracker(slideNumber)
    gesture2.addStateTracker(pointer)
    gesture3.addStateTracker(annotation)
    gesture4.addStateTracker(eraser)

    handTracker.add_gesture(gesture1)
    handTracker.add_gesture(gesture2)
    handTracker.add_gesture(gesture3)
    handTracker.add_gesture(gesture4)

    slideNumber.setOnUpdate(set_slide_number)
    pointer.setOnUpdate(show_pointer)

    # displayManager.load_from_pptx('test2.pptx')
    displayManager.load_folder('test')

    trackerThread = Thread(target=runner.loop, args=[handTracker])

    trackerThread.start()

    displayManager.runLoop()
