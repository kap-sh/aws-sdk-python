"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#Iso8601Timestamp``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_networkflowmonitor.errors import DeserializationError
from aws_sdk_networkflowmonitor._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

Iso8601Timestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: Iso8601Timestamp) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> Iso8601Timestamp:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)