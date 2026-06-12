"""Generated from Smithy shape ``com.amazonaws.qbusiness#ActionPayloadFieldType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_qbusiness.errors import DeserializationError
from aws_sdk_qbusiness._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ActionPayloadFieldType: TypeAlias = Literal["STRING", "NUMBER", "ARRAY", "BOOLEAN",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("STRING", "NUMBER", "ARRAY", "BOOLEAN",))


def serialize_json(value: ActionPayloadFieldType) -> str:
    return value


def deserialize_json(data: str) -> ActionPayloadFieldType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActionPayloadFieldType value: {data!r}")
    return cast(ActionPayloadFieldType, data)