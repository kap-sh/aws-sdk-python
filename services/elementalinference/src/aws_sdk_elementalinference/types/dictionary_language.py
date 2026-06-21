"""Generated from Smithy shape ``com.amazonaws.elementalinference#DictionaryLanguage``."""

from typing import Literal, TypeAlias, cast

DictionaryLanguage: TypeAlias = Literal[
    "eng",
    "fra",
    "ita",
    "deu",
    "spa",
    "por",
]


# --- restJson1 ser/de ---
def serialize_json(value: DictionaryLanguage) -> str:
    return value


def deserialize_json(data: str) -> DictionaryLanguage:
    return cast(DictionaryLanguage, data)
