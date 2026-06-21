"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#TranscribeVocabularyFilterMethod``."""

from typing import Literal, TypeAlias, cast

TranscribeVocabularyFilterMethod: TypeAlias = Literal[
    "remove",
    "mask",
    "tag",
]


# --- restJson1 ser/de ---
def serialize_json(value: TranscribeVocabularyFilterMethod) -> str:
    return value


def deserialize_json(data: str) -> TranscribeVocabularyFilterMethod:
    return cast(TranscribeVocabularyFilterMethod, data)
