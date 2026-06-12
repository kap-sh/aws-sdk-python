"""Generated from Smithy shape ``com.amazonaws.elementalinference#DictionaryLanguage``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elementalinference.errors import DeserializationError

DictionaryLanguage: TypeAlias = Literal[
    "eng",
    "fra",
    "ita",
    "deu",
    "spa",
    "por",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "eng",
        "fra",
        "ita",
        "deu",
        "spa",
        "por",
    )
)


def serialize_json(value: DictionaryLanguage) -> str:
    return value


def deserialize_json(data: str) -> DictionaryLanguage:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DictionaryLanguage value: {data!r}")
    return cast(DictionaryLanguage, data)
