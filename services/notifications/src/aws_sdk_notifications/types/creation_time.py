"""Generated from Smithy shape ``com.amazonaws.notifications#CreationTime``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_notifications.errors import DeserializationError
from aws_sdk_notifications._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

CreationTime: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: CreationTime) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> CreationTime:
    return datetime.datetime.fromisoformat(data)