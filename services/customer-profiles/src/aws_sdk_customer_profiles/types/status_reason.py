"""Generated from Smithy shape ``com.amazonaws.customerprofiles#StatusReason``."""

from typing import Literal, TypeAlias, cast

StatusReason: TypeAlias = Literal[
    "VALIDATION_FAILURE",
    "INTERNAL_FAILURE",
]


# --- restJson1 ser/de ---
def serialize_json(value: StatusReason) -> str:
    return value


def deserialize_json(data: str) -> StatusReason:
    return cast(StatusReason, data)
