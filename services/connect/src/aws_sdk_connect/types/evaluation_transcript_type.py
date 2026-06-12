"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationTranscriptType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

EvaluationTranscriptType: TypeAlias = Literal[
    "RAW",
    "REDACTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RAW",
        "REDACTED",
    )
)


def serialize_json(value: EvaluationTranscriptType) -> str:
    return value


def deserialize_json(data: str) -> EvaluationTranscriptType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EvaluationTranscriptType value: {data!r}")
    return cast(EvaluationTranscriptType, data)
