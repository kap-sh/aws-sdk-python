"""Generated from Smithy shape ``com.amazonaws.datazone#TriggerSourceType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>The type of trigger source for a notebook run in Amazon SageMaker Unified Studio.</p>"""
TriggerSourceType: TypeAlias = Literal[
    "MANUAL",
    "SCHEDULED",
    "WORKFLOW",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MANUAL",
        "SCHEDULED",
        "WORKFLOW",
    )
)


def serialize_json(value: TriggerSourceType) -> str:
    return value


def deserialize_json(data: str) -> TriggerSourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TriggerSourceType value: {data!r}")
    return cast(TriggerSourceType, data)
