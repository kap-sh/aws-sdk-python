"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CustomVocabularyStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

CustomVocabularyStatus: TypeAlias = Literal[
    "Ready",
    "Deleting",
    "Exporting",
    "Importing",
    "Creating",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Ready",
        "Deleting",
        "Exporting",
        "Importing",
        "Creating",
    )
)


def serialize_json(value: CustomVocabularyStatus) -> str:
    return value


def deserialize_json(data: str) -> CustomVocabularyStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CustomVocabularyStatus value: {data!r}")
    return cast(CustomVocabularyStatus, data)
