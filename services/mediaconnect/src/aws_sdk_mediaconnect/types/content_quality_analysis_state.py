"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ContentQualityAnalysisState``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_mediaconnect.errors import DeserializationError
from aws_sdk_mediaconnect._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ContentQualityAnalysisState: TypeAlias = Literal["ENABLED", "DISABLED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ENABLED", "DISABLED",))


def serialize_json(value: ContentQualityAnalysisState) -> str:
    return value


def deserialize_json(data: str) -> ContentQualityAnalysisState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContentQualityAnalysisState value: {data!r}")
    return cast(ContentQualityAnalysisState, data)