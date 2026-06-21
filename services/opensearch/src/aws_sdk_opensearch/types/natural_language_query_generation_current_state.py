"""Generated from Smithy shape ``com.amazonaws.opensearch#NaturalLanguageQueryGenerationCurrentState``."""

from typing import Literal, TypeAlias, cast

NaturalLanguageQueryGenerationCurrentState: TypeAlias = Literal[
    "NOT_ENABLED",
    "ENABLE_COMPLETE",
    "ENABLE_IN_PROGRESS",
    "ENABLE_FAILED",
    "DISABLE_COMPLETE",
    "DISABLE_IN_PROGRESS",
    "DISABLE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: NaturalLanguageQueryGenerationCurrentState) -> str:
    return value


def deserialize_json(data: str) -> NaturalLanguageQueryGenerationCurrentState:
    return cast(NaturalLanguageQueryGenerationCurrentState, data)
