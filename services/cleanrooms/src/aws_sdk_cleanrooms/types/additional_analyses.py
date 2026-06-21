"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AdditionalAnalyses``."""

from typing import Literal, TypeAlias, cast

AdditionalAnalyses: TypeAlias = Literal[
    "ALLOWED",
    "REQUIRED",
    "NOT_ALLOWED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalAnalyses) -> str:
    return value


def deserialize_json(data: str) -> AdditionalAnalyses:
    return cast(AdditionalAnalyses, data)
