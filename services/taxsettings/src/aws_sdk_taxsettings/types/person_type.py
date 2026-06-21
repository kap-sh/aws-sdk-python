"""Generated from Smithy shape ``com.amazonaws.taxsettings#PersonType``."""

from typing import Literal, TypeAlias, cast

PersonType: TypeAlias = Literal[
    "Legal Person",
    "Physical Person",
    "Business",
]


# --- restJson1 ser/de ---
def serialize_json(value: PersonType) -> str:
    return value


def deserialize_json(data: str) -> PersonType:
    return cast(PersonType, data)
