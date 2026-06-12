"""Generated from Smithy shape ``com.amazonaws.bedrock#ByteContentBlob``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock.errors import DeserializationError
from aws_sdk_bedrock._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ByteContentBlob: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: ByteContentBlob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> ByteContentBlob:
    return base64.b64decode(data)
