"""Generated from Smithy shape ``com.amazonaws.sesv2#ContactLanguage``."""

from typing import Literal, TypeAlias, cast

ContactLanguage: TypeAlias = Literal[
    "EN",
    "JA",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactLanguage) -> str:
    return value


def deserialize_json(data: str) -> ContactLanguage:
    return cast(ContactLanguage, data)
