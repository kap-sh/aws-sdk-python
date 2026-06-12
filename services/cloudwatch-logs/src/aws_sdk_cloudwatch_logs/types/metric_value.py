"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#MetricValue``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_cloudwatch_logs.errors import DeserializationError
from aws_sdk_cloudwatch_logs._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>The value to publish to the CloudWatch metric. For example, if you're counting the occurrences of a term like <code>Error</code>, the value is <code>1</code> for each occurrence. If you're counting the bytes transferred, the value is the value in the log event.</p>"""
MetricValue: TypeAlias = str
