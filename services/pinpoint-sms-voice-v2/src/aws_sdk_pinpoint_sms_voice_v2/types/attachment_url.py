"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#AttachmentUrl``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError
from aws_sdk_pinpoint_sms_voice_v2._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AttachmentUrl: TypeAlias = str