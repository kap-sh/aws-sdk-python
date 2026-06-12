"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ImportResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

ImportResourceType: TypeAlias = Literal[
    "Bot",
    "BotLocale",
    "CustomVocabulary",
    "TestSet",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Bot",
        "BotLocale",
        "CustomVocabulary",
        "TestSet",
    )
)


def serialize_json(value: ImportResourceType) -> str:
    return value


def deserialize_json(data: str) -> ImportResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImportResourceType value: {data!r}")
    return cast(ImportResourceType, data)
