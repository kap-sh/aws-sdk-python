"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#ScopeStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_networkflowmonitor.errors import DeserializationError
from aws_sdk_networkflowmonitor._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ScopeStatus: TypeAlias = Literal["SUCCEEDED", "IN_PROGRESS", "FAILED", "DEACTIVATING", "DEACTIVATED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SUCCEEDED", "IN_PROGRESS", "FAILED", "DEACTIVATING", "DEACTIVATED",))


def serialize_json(value: ScopeStatus) -> str:
    return value


def deserialize_json(data: str) -> ScopeStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScopeStatus value: {data!r}")
    return cast(ScopeStatus, data)