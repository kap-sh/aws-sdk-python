"""Generated from Smithy shape ``com.amazonaws.connect#VocabularyState``."""

from typing import Literal, TypeAlias, cast

VocabularyState: TypeAlias = Literal[
    "CREATION_IN_PROGRESS",
    "ACTIVE",
    "CREATION_FAILED",
    "DELETE_IN_PROGRESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: VocabularyState) -> str:
    return value


def deserialize_json(data: str) -> VocabularyState:
    return cast(VocabularyState, data)
