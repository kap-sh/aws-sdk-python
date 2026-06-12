"""Generated from Smithy shape ``com.amazonaws.bedrock#CustomizationType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock.errors import DeserializationError
from aws_sdk_bedrock._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

CustomizationType: TypeAlias = Literal[
    "FINE_TUNING",
    "CONTINUED_PRE_TRAINING",
    "DISTILLATION",
    "REINFORCEMENT_FINE_TUNING",
    "IMPORTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FINE_TUNING",
        "CONTINUED_PRE_TRAINING",
        "DISTILLATION",
        "REINFORCEMENT_FINE_TUNING",
        "IMPORTED",
    )
)


def serialize_json(value: CustomizationType) -> str:
    return value


def deserialize_json(data: str) -> CustomizationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CustomizationType value: {data!r}")
    return cast(CustomizationType, data)
