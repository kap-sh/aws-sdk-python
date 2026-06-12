"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#TranscribePartialResultsStability``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_meetings.errors import DeserializationError

TranscribePartialResultsStability: TypeAlias = Literal[
    "low",
    "medium",
    "high",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "low",
        "medium",
        "high",
    )
)


def serialize_json(value: TranscribePartialResultsStability) -> str:
    return value


def deserialize_json(data: str) -> TranscribePartialResultsStability:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TranscribePartialResultsStability value: {data!r}"
        )
    return cast(TranscribePartialResultsStability, data)
