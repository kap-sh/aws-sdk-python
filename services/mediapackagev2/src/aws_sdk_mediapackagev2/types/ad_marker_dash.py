"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#AdMarkerDash``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_mediapackagev2.errors import DeserializationError
from aws_sdk_mediapackagev2._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AdMarkerDash: TypeAlias = Literal["BINARY", "XML",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("BINARY", "XML",))


def serialize_json(value: AdMarkerDash) -> str:
    return value


def deserialize_json(data: str) -> AdMarkerDash:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AdMarkerDash value: {data!r}")
    return cast(AdMarkerDash, data)