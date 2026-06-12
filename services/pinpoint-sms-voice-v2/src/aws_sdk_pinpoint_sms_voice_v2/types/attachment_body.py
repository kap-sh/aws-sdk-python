"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#AttachmentBody``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError
from aws_sdk_pinpoint_sms_voice_v2._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AttachmentBody: TypeAlias = bytes


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AttachmentBody) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_0(data: str) -> AttachmentBody:
    return base64.b64decode(data)