"""Generated from Smithy shape ``com.amazonaws.elementalinference#TranscriptionLanguage``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elementalinference.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "eng",
        "eng-au",
        "eng-gb",
        "eng-us",
        "fra",
        "ita",
        "deu",
        "spa",
        "por",
    )
)


def serialize_json(value: TranscriptionLanguage) -> str:
    return value


def deserialize_json(data: str) -> TranscriptionLanguage:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TranscriptionLanguage value: {data!r}")
    return cast(TranscriptionLanguage, data)
