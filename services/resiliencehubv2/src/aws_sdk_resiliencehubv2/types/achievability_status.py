"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#AchievabilityStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_resiliencehubv2.errors import DeserializationError
from aws_sdk_resiliencehubv2._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AchievabilityStatus: TypeAlias = Literal["ACHIEVABLE", "NOT_ACHIEVABLE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ACHIEVABLE", "NOT_ACHIEVABLE",))


def serialize_json(value: AchievabilityStatus) -> str:
    return value


def deserialize_json(data: str) -> AchievabilityStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AchievabilityStatus value: {data!r}")
    return cast(AchievabilityStatus, data)