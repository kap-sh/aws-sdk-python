"""Generated from Smithy shape ``com.amazonaws.qbusiness#AttributeType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_qbusiness.errors import DeserializationError
from aws_sdk_qbusiness._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AttributeType: TypeAlias = Literal["STRING", "STRING_LIST", "NUMBER", "DATE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("STRING", "STRING_LIST", "NUMBER", "DATE",))


def serialize_json(value: AttributeType) -> str:
    return value


def deserialize_json(data: str) -> AttributeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AttributeType value: {data!r}")
    return cast(AttributeType, data)