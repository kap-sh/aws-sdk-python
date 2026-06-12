"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentAttributeBoostingLevel``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_qbusiness.errors import DeserializationError
from aws_sdk_qbusiness._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

DocumentAttributeBoostingLevel: TypeAlias = Literal["NONE", "LOW", "MEDIUM", "HIGH", "VERY_HIGH", "ONE", "TWO",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("NONE", "LOW", "MEDIUM", "HIGH", "VERY_HIGH", "ONE", "TWO",))


def serialize_json(value: DocumentAttributeBoostingLevel) -> str:
    return value


def deserialize_json(data: str) -> DocumentAttributeBoostingLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DocumentAttributeBoostingLevel value: {data!r}")
    return cast(DocumentAttributeBoostingLevel, data)