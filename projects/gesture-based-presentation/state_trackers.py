from gestureflow.definitions import *

class AnnotationTracker():
    def __init__(self, displayManager) -> None:
        self.prev_position = None
        self.displayManager = displayManager

    def update(self, state):
        if state[GESTURE_FOUND]:
            cur_position = tuple(state[FINGER_POINTS][1])
            if self.prev_position:
                self.displayManager.annotate(self.prev_position, cur_position)
            self.prev_position = cur_position
        else:
            self.prev_position = None


class EraserTracker():
    def __init__(self, displayManager) -> None:
        self.prev_position = None
        self.displayManager = displayManager

    def update(self, state):
        if state[GESTURE_FOUND]:
            cur_position = tuple(state[HAND_CENTER])
            self.displayManager.erase_point(cur_position)
            self.prev_position = cur_position
        else:
            self.prev_position = None