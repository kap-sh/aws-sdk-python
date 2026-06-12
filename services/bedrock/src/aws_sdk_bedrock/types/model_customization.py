"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelCustomization``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock.errors import DeserializationError
from aws_sdk_bedrock._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ModelCustomization: TypeAlias = Literal[
    "FINE_TUNING",
    "CONTINUED_PRE_TRAINING",
    "DISTILLATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FINE_TUNING",
        "CONTINUED_PRE_TRAINING",
        "DISTILLATION",
    )
)


def serialize_json(value: ModelCustomization) -> str:
    return value


def deserialize_json(data: str) -> ModelCustomization:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelCustomization value: {data!r}")
    return cast(ModelCustomization, data)
