"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#Pronouns``."""

from typing import Literal, TypeAlias, cast

Pronouns: TypeAlias = Literal[
    "HE_HIM",
    "SHE_HER",
    "THEY_THEM",
]


# --- restJson1 ser/de ---
def serialize_json(value: Pronouns) -> str:
    return value


def deserialize_json(data: str) -> Pronouns:
    return cast(Pronouns, data)
