"""Generated from Smithy shape ``com.amazonaws.groundstation#AuditResults``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_groundstation.errors import DeserializationError
from aws_sdk_groundstation._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AuditResults: TypeAlias = Literal["HEALTHY", "UNHEALTHY",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("HEALTHY", "UNHEALTHY",))


def serialize_json(value: AuditResults) -> str:
    return value


def deserialize_json(data: str) -> AuditResults:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuditResults value: {data!r}")
    return cast(AuditResults, data)