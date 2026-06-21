"""Generated from Smithy shape ``com.amazonaws.taxsettings#CustomerType``."""

from typing import Literal, TypeAlias, cast

CustomerType: TypeAlias = Literal[
    "Business",
    "Individual",
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomerType) -> str:
    return value


def deserialize_json(data: str) -> CustomerType:
    return cast(CustomerType, data)
