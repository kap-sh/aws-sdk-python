"""Generated from Smithy shape ``com.amazonaws.opensearch#NaturalLanguageQueryGenerationDesiredState``."""

from typing import Literal, TypeAlias, cast

NaturalLanguageQueryGenerationDesiredState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: NaturalLanguageQueryGenerationDesiredState) -> str:
    return value


def deserialize_json(data: str) -> NaturalLanguageQueryGenerationDesiredState:
    return cast(NaturalLanguageQueryGenerationDesiredState, data)
