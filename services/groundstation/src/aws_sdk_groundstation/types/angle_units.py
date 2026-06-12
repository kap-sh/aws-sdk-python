"""Generated from Smithy shape ``com.amazonaws.groundstation#AngleUnits``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_groundstation.errors import DeserializationError
from aws_sdk_groundstation._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AngleUnits: TypeAlias = Literal["DEGREE_ANGLE", "RADIAN",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DEGREE_ANGLE", "RADIAN",))


def serialize_json(value: AngleUnits) -> str:
    return value


def deserialize_json(data: str) -> AngleUnits:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AngleUnits value: {data!r}")
    return cast(AngleUnits, data)