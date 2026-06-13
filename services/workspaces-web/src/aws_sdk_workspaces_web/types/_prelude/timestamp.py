"""Generated from Smithy prelude shape ``smithy.api#Timestamp``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, cast
from aws_sdk_workspaces_web.errors import DeserializationError
from aws_sdk_workspaces_web._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

# --- restJson1 ser/de ---
def serialize_json(value: datetime.datetime) -> float:
    return value.timestamp()


def deserialize_json(data: float) -> datetime.datetime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)