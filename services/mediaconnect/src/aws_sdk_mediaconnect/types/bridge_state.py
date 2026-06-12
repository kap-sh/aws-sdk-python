"""Generated from Smithy shape ``com.amazonaws.mediaconnect#BridgeState``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_mediaconnect.errors import DeserializationError
from aws_sdk_mediaconnect._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

BridgeState: TypeAlias = Literal["CREATING", "STANDBY", "STARTING", "DEPLOYING", "ACTIVE", "STOPPING", "DELETING", "DELETED", "START_FAILED", "START_PENDING", "STOP_FAILED", "UPDATING",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CREATING", "STANDBY", "STARTING", "DEPLOYING", "ACTIVE", "STOPPING", "DELETING", "DELETED", "START_FAILED", "START_PENDING", "STOP_FAILED", "UPDATING",))


def serialize_json(value: BridgeState) -> str:
    return value


def deserialize_json(data: str) -> BridgeState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BridgeState value: {data!r}")
    return cast(BridgeState, data)