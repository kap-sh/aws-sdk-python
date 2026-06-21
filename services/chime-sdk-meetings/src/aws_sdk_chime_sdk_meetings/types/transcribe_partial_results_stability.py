"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#TranscribePartialResultsStability``."""

from typing import Literal, TypeAlias, cast

TranscribePartialResultsStability: TypeAlias = Literal[
    "low",
    "medium",
    "high",
]


# --- restJson1 ser/de ---
def serialize_json(value: TranscribePartialResultsStability) -> str:
    return value


def deserialize_json(data: str) -> TranscribePartialResultsStability:
    return cast(TranscribePartialResultsStability, data)
