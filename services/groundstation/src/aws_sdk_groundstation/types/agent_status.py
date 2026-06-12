"""Generated from Smithy shape ``com.amazonaws.groundstation#AgentStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_groundstation.errors import DeserializationError
from aws_sdk_groundstation._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AgentStatus: TypeAlias = Literal["SUCCESS", "FAILED", "ACTIVE", "INACTIVE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SUCCESS", "FAILED", "ACTIVE", "INACTIVE",))


def serialize_json(value: AgentStatus) -> str:
    return value


def deserialize_json(data: str) -> AgentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AgentStatus value: {data!r}")
    return cast(AgentStatus, data)