"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#StyleType``."""

from typing import Literal, TypeAlias, cast

StyleType: TypeAlias = Literal[
    "Default",
    "SpellByLetter",
    "SpellByWord",
]


# --- restJson1 ser/de ---
def serialize_json(value: StyleType) -> str:
    return value


def deserialize_json(data: str) -> StyleType:
    return cast(StyleType, data)
