"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ImportResourceType``."""

from typing import Literal, TypeAlias, cast

ImportResourceType: TypeAlias = Literal[
    "Bot",
    "BotLocale",
    "CustomVocabulary",
    "TestSet",
]


# --- restJson1 ser/de ---
def serialize_json(value: ImportResourceType) -> str:
    return value


def deserialize_json(data: str) -> ImportResourceType:
    return cast(ImportResourceType, data)
