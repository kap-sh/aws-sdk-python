"""Generated from Smithy shape ``com.amazonaws.taxsettings#IsraelCustomerType``."""

from typing import Literal, TypeAlias, cast

IsraelCustomerType: TypeAlias = Literal[
    "Business",
    "Individual",
]


# --- restJson1 ser/de ---
def serialize_json(value: IsraelCustomerType) -> str:
    return value


def deserialize_json(data: str) -> IsraelCustomerType:
    return cast(IsraelCustomerType, data)
