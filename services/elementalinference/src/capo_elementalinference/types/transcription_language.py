"""Generated from Smithy shape ``com.amazonaws.elementalinference#TranscriptionLanguage``."""

from typing import Literal, TypeAlias, cast

TranscriptionLanguage: TypeAlias = Literal[
    "eng",
    "eng-au",
    "eng-gb",
    "eng-us",
    "fra",
    "ita",
    "deu",
    "spa",
    "por",
]


# --- restJson1 ser/de ---
def serialize_json(value: TranscriptionLanguage) -> str:
    return value


def deserialize_json(data: str) -> TranscriptionLanguage:
    return cast(TranscriptionLanguage, data)
