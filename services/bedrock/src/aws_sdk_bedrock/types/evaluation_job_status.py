"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationJobStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock.errors import DeserializationError
from aws_sdk_bedrock._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

EvaluationJobStatus: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
    "Stopping",
    "Stopped",
    "Deleting",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InProgress",
        "Completed",
        "Failed",
        "Stopping",
        "Stopped",
        "Deleting",
    )
)


def serialize_json(value: EvaluationJobStatus) -> str:
    return value


def deserialize_json(data: str) -> EvaluationJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EvaluationJobStatus value: {data!r}")
    return cast(EvaluationJobStatus, data)
