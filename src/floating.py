#!/usr/bin/python3

from gi.repository import Gtk
import random
import status

from util import trackers
from util import settings

POSITIONING_TIMEOUT = 30
ALIGNMENTS = [int(Gtk.Align.START), int(Gtk.Align.END), int(Gtk.Align.CENTER)]

class Floating:
    def __init__(self, initial_monitor=0):
        super(Floating, self).__init__()
        self.set_halign(Gtk.Align.END)
        self.set_valign(Gtk.Align.CENTER)
        self.current_monitor = initial_monitor

    def start_positioning(self):
        self.show()
        if settings.get_allow_floating():
            trackers.timer_tracker_get().cancel(str(self) + "positioning")
            trackers.timer_tracker_get().start_seconds(str(self) + "positioning",
                                                       POSITIONING_TIMEOUT,
                                                       self.positioning_callback)

    def stop_positioning(self):
        if settings.get_allow_floating():
            trackers.timer_tracker_get().cancel(str(self) + "positioning")

    def positioning_callback(self):
        self.queue_resize()
        return True
