#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Archive Replay Plutosdr
# GNU Radio version: 3.8.5.0

from gnuradio import blocks
import pmt
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import iio


class archive_replay_plutosdr(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Archive Replay Plutosdr")

        ##################################################
        # Variables
        ##################################################
        self.tx_gain = tx_gain = 64
        self.tx_frequency = tx_frequency = 2425.715e6
        self.tx_channel = tx_channel = ""
        self.sample_rate = sample_rate = 4e6
        self.ip_address = ip_address = "192.168.2.1"
        self.filepath = filepath = ""

        ##################################################
        # Blocks
        ##################################################
        self.iio_pluto_sink_0 = iio.pluto_sink("ip:" + str(ip_address), int(tx_frequency), int(sample_rate), 20000000, 32768, False, 89.75 - tx_gain, '', True)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, filepath, True, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.iio_pluto_sink_0, 0))


    def get_tx_gain(self):
        return self.tx_gain

    def set_tx_gain(self, tx_gain):
        self.tx_gain = tx_gain
        self.iio_pluto_sink_0.set_params(int(self.tx_frequency), int(self.sample_rate), 20000000, 89.75 - self.tx_gain, '', True)

    def get_tx_frequency(self):
        return self.tx_frequency

    def set_tx_frequency(self, tx_frequency):
        self.tx_frequency = tx_frequency
        self.iio_pluto_sink_0.set_params(int(self.tx_frequency), int(self.sample_rate), 20000000, 89.75 - self.tx_gain, '', True)

    def get_tx_channel(self):
        return self.tx_channel

    def set_tx_channel(self, tx_channel):
        self.tx_channel = tx_channel

    def get_sample_rate(self):
        return self.sample_rate

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate
        self.iio_pluto_sink_0.set_params(int(self.tx_frequency), int(self.sample_rate), 20000000, 89.75 - self.tx_gain, '', True)

    def get_ip_address(self):
        return self.ip_address

    def set_ip_address(self, ip_address):
        self.ip_address = ip_address

    def get_filepath(self):
        return self.filepath

    def set_filepath(self, filepath):
        self.filepath = filepath
        self.blocks_file_source_0.open(self.filepath, True)





def main(top_block_cls=archive_replay_plutosdr, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()

    tb.wait()


if __name__ == '__main__':
    main()
