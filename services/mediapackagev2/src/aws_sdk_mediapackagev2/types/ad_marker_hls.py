"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#AdMarkerHls``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_mediapackagev2.errors import DeserializationError
from aws_sdk_mediapackagev2._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AdMarkerHls: TypeAlias = Literal["DATERANGE", "SCTE35_ENHANCED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DATERANGE", "SCTE35_ENHANCED",))


def serialize_json(value: AdMarkerHls) -> str:
    return value


def deserialize_json(data: str) -> AdMarkerHls:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AdMarkerHls value: {data!r}")
    return cast(AdMarkerHls, data)