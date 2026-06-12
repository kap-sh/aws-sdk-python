"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#EpochMillis``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_cloudwatch_logs.errors import DeserializationError
from aws_sdk_cloudwatch_logs._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

EpochMillis: TypeAlias = int

DEFAULT_EPOCH_MILLIS: EpochMillis = 0
