"""Generated from Smithy shape ``com.amazonaws.appintegrations#ExecutionStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_appintegrations.errors import DeserializationError
from aws_sdk_appintegrations._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ExecutionStatus: TypeAlias = Literal["COMPLETED", "IN_PROGRESS", "FAILED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("COMPLETED", "IN_PROGRESS", "FAILED",))


def serialize_json(value: ExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> ExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionStatus value: {data!r}")
    return cast(ExecutionStatus, data)