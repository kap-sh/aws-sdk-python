"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#VocabularyFilterMethod``."""

from typing import Literal, TypeAlias, cast

VocabularyFilterMethod: TypeAlias = Literal[
    "remove",
    "mask",
    "tag",
]


# --- restJson1 ser/de ---
def serialize_json(value: VocabularyFilterMethod) -> str:
    return value


def deserialize_json(data: str) -> VocabularyFilterMethod:
    return cast(VocabularyFilterMethod, data)
