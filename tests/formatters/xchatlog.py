#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Tests for the XChat log file event formatter."""

import unittest

from plaso.formatters import xchatlog

from tests.formatters import test_lib


class XChatLogFormatterTest(test_lib.EventFormatterTestCase):
  """Tests for the XChat log file entry event formatter."""

  def testInitialization(self):
    """Tests the initialization."""
    event_formatter = xchatlog.XChatLogFormatter()
    self.assertIsNotNone(event_formatter)

  def testGetFormatStringAttributeNames(self):
    """Tests the GetFormatStringAttributeNames function."""
    event_formatter = xchatlog.XChatLogFormatter()

    expected_attribute_names = [
        u'nickname',
        u'text']

    self._TestGetFormatStringAttributeNames(
        event_formatter, expected_attribute_names)

  # TODO: add test for GetMessages.


if __name__ == '__main__':
  unittest.main()
