"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#PartialResultsStability``."""

from typing import Literal, TypeAlias, cast

PartialResultsStability: TypeAlias = Literal[
    "high",
    "medium",
    "low",
]


# --- restJson1 ser/de ---
def serialize_json(value: PartialResultsStability) -> str:
    return value


def deserialize_json(data: str) -> PartialResultsStability:
    return cast(PartialResultsStability, data)
