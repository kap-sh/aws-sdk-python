"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalScribeVocabularyFilterMethod``."""

from typing import Literal, TypeAlias, cast

MedicalScribeVocabularyFilterMethod: TypeAlias = Literal[
    "remove",
    "mask",
    "tag",
]


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeVocabularyFilterMethod) -> str:
    return value


def deserialize_json(data: str) -> MedicalScribeVocabularyFilterMethod:
    return cast(MedicalScribeVocabularyFilterMethod, data)
