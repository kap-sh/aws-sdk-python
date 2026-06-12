"""Generated from Smithy shape ``com.amazonaws.qbusiness#AttributeValueOperator``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_qbusiness.errors import DeserializationError
from aws_sdk_qbusiness._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AttributeValueOperator: TypeAlias = Literal["DELETE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DELETE",))


def serialize_json(value: AttributeValueOperator) -> str:
    return value


def deserialize_json(data: str) -> AttributeValueOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AttributeValueOperator value: {data!r}")
    return cast(AttributeValueOperator, data)