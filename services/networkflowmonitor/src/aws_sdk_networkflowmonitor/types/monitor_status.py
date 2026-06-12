"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#MonitorStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_networkflowmonitor.errors import DeserializationError
from aws_sdk_networkflowmonitor._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

MonitorStatus: TypeAlias = Literal["PENDING", "ACTIVE", "INACTIVE", "ERROR", "DELETING",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PENDING", "ACTIVE", "INACTIVE", "ERROR", "DELETING",))


def serialize_json(value: MonitorStatus) -> str:
    return value


def deserialize_json(data: str) -> MonitorStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MonitorStatus value: {data!r}")
    return cast(MonitorStatus, data)