"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#TranscribeVocabularyFilterMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_meetings.errors import DeserializationError

TranscribeVocabularyFilterMethod: TypeAlias = Literal[
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


def serialize_json(value: TranscribeVocabularyFilterMethod) -> str:
    return value


def deserialize_json(data: str) -> TranscribeVocabularyFilterMethod:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TranscribeVocabularyFilterMethod value: {data!r}"
        )
    return cast(TranscribeVocabularyFilterMethod, data)
