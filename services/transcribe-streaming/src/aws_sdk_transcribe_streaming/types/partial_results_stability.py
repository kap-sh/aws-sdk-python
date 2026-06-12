"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#PartialResultsStability``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe_streaming.errors import DeserializationError

PartialResultsStability: TypeAlias = Literal[
    "high",
    "medium",
    "low",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "high",
        "medium",
        "low",
    )
)


def serialize_json(value: PartialResultsStability) -> str:
    return value


def deserialize_json(data: str) -> PartialResultsStability:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PartialResultsStability value: {data!r}")
    return cast(PartialResultsStability, data)
