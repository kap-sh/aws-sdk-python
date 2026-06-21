"""Generated from Smithy shape ``com.amazonaws.connect#ViewType``."""

from typing import Literal, TypeAlias, cast

ViewType: TypeAlias = Literal[
    "CUSTOMER_MANAGED",
    "AWS_MANAGED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ViewType) -> str:
    return value


def deserialize_json(data: str) -> ViewType:
    return cast(ViewType, data)
