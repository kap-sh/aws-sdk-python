"""Generated from Smithy shape ``com.amazonaws.bedrock#Timestamp``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock.errors import DeserializationError
from aws_sdk_bedrock._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

Timestamp: TypeAlias = datetime.datetime


# --- restJson1 ser/de ---
def serialize_json(value: Timestamp) -> str:
    return value.isoformat()


def deserialize_json(data: str) -> Timestamp:
    return datetime.datetime.fromisoformat(data)
