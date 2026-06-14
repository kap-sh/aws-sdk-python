"""Generated from Smithy shape ``com.amazonaws.appintegrations#ExecutionMode``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_appintegrations.errors import DeserializationError
from aws_sdk_appintegrations._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ExecutionMode: TypeAlias = Literal["ON_DEMAND", "SCHEDULED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ON_DEMAND", "SCHEDULED",))


def serialize_json(value: ExecutionMode) -> str:
    return value


def deserialize_json(data: str) -> ExecutionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionMode value: {data!r}")
    return cast(ExecutionMode, data)