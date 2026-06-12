"""Generated from Smithy shape ``com.amazonaws.securityir#ActionType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_security_ir.errors import DeserializationError
from aws_sdk_security_ir._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ActionType: TypeAlias = Literal["Evidence", "Investigation", "Summarization",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Evidence", "Investigation", "Summarization",))


def serialize_json(value: ActionType) -> str:
    return value


def deserialize_json(data: str) -> ActionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActionType value: {data!r}")
    return cast(ActionType, data)