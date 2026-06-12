"""Generated from Smithy shape ``com.amazonaws.notifications#LastActivationTime``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_notifications.errors import DeserializationError
from aws_sdk_notifications._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

LastActivationTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: LastActivationTime) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> LastActivationTime:
    return datetime.datetime.fromisoformat(data)