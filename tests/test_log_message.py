"""Tests for the reader.feed module"""
import unittest
from common_services import create_log_message
from Context_class import context_class_object
import os

class TestLogMessage(unittest.TestCase):
    def test_info(self):
        ctx = context_class_object()
        log = create_log_message.CreateAuditMessage(context=ctx)
        log.createauditmessage(business_key="test",business_value="test",log_level="INFO",trace_id="12334",information="this is a info message",message="received")

    def test_error(self):
        ctx = context_class_object()
        log = create_log_message.CreateAuditMessage(context=ctx)
        log.createauditmessage(business_key="test",business_value="test",log_level="ERROR",trace_id="12334",information="this is an error message",message="received")

    def test_debug(self):
        ctx = context_class_object()
        os.environ["DEBUG"] = "true"
        log = create_log_message.CreateAuditMessage(context=ctx)
        log.createauditmessage(business_key="test",business_value="test",log_level="DEBUG",trace_id="12334",information="this is a debug message",message="received")