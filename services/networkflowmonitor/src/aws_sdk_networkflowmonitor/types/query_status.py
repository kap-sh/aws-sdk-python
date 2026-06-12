"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#QueryStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_networkflowmonitor.errors import DeserializationError
from aws_sdk_networkflowmonitor._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

QueryStatus: TypeAlias = Literal["QUEUED", "RUNNING", "SUCCEEDED", "FAILED", "CANCELED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("QUEUED", "RUNNING", "SUCCEEDED", "FAILED", "CANCELED",))


def serialize_json(value: QueryStatus) -> str:
    return value


def deserialize_json(data: str) -> QueryStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QueryStatus value: {data!r}")
    return cast(QueryStatus, data)