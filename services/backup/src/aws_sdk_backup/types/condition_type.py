"""Generated from Smithy shape ``com.amazonaws.backup#ConditionType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_backup.errors import DeserializationError
from aws_sdk_backup._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ConditionType: TypeAlias = Literal["STRINGEQUALS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("STRINGEQUALS",))


def serialize_json(value: ConditionType) -> str:
    return value


def deserialize_json(data: str) -> ConditionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConditionType value: {data!r}")
    return cast(ConditionType, data)