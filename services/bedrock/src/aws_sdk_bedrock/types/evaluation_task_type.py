"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationTaskType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock.errors import DeserializationError
from aws_sdk_bedrock._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

EvaluationTaskType: TypeAlias = Literal[
    "Summarization",
    "Classification",
    "QuestionAndAnswer",
    "Generation",
    "Custom",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Summarization",
        "Classification",
        "QuestionAndAnswer",
        "Generation",
        "Custom",
    )
)


def serialize_json(value: EvaluationTaskType) -> str:
    return value


def deserialize_json(data: str) -> EvaluationTaskType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EvaluationTaskType value: {data!r}")
    return cast(EvaluationTaskType, data)
