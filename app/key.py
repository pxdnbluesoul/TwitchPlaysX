#http://stackoverflow.com/questions/1823762/sendkeys-for-python-3-1-on-windows

import win32api
import win32con
import win32ui
import time,sys

keyDelay = 10.0 # Seconds
keymap = {
    "up": win32con.VK_UP,
    "left": win32con.VK_LEFT,
    "down": win32con.VK_DOWN,
    "right": win32con.VK_RIGHT,
    "bksp": win32con.VK_BACK,
	"delete": win32con.VK_DELETE,
	"blackbox": ord("█")
    "a": ord("a"),
    "b": ord("b"),
    "c": ord("c"),
    "d": ord("d"),
    "e": ord("e"),
    "f": ord("f"),
    "g": ord("g"),
    "h": ord("h"),
    "i": ord("i"),
    "j": ord("j"),
    "k": ord("k"),
    "l": ord("l"),
    "m": ord("m"),
    "n": ord("n"),
    "o": ord("o"),
    "p": ord("p"),
    "q": ord("q"),
    "r": ord("r"),
    "s": ord("s"),
    "t": ord("t"),
    "u": ord("u"),
    "v": ord("v"),
    "w": ord("w"),
    "x": ord("x"),
    "y": ord("y"),
    "z": ord("z"),
    "A": ord("A"),
    "B": ord("B"),
    "C": ord("C"),
    "D": ord("D"),
    "E": ord("E"),
    "F": ord("F"),
    "G": ord("G"),
    "H": ord("H"),
    "I": ord("I"),
    "J": ord("J"),
    "K": ord("K"),
    "L": ord("L"),
    "M": ord("M"),
    "N": ord("N"),
    "O": ord("O"),
    "P": ord("P"),
    "Q": ord("Q"),
    "R": ord("R"),
    "S": ord("S"),
    "T": ord("T"),
    "U": ord("U"),
    "V": ord("V"),
    "W": ord("W"),
    "X": ord("X"),
    "Y": ord("Y"),
    "Z": ord("Z"),
}

def sendKey(button):
    win32api.keybd_event(keymap[button], 0, 0, 0)
    time.sleep(keyDelay)
    win32api.keybd_event(keymap[button], 0, win32con.KEYEVENTF_KEYUP, 0)

if __name__ == "__main__":
    win = win32ui.FindWindow(None, sys.argv[1])
    win.SetForegroundWindow()
    win.SetFocus()
    sendKey(sys.argv[2])
