"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalScribeVocabularyFilterMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe_streaming.errors import DeserializationError

MedicalScribeVocabularyFilterMethod: TypeAlias = Literal[
    "remove",
    "mask",
    "tag",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "remove",
        "mask",
        "tag",
    )
)


def serialize_json(value: MedicalScribeVocabularyFilterMethod) -> str:
    return value


def deserialize_json(data: str) -> MedicalScribeVocabularyFilterMethod:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MedicalScribeVocabularyFilterMethod value: {data!r}"
        )
    return cast(MedicalScribeVocabularyFilterMethod, data)
