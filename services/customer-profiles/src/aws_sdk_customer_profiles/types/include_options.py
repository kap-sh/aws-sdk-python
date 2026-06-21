"""Generated from Smithy shape ``com.amazonaws.customerprofiles#IncludeOptions``."""

from typing import Literal, TypeAlias, cast

IncludeOptions: TypeAlias = Literal[
    "ALL",
    "ANY",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: IncludeOptions) -> str:
    return value


def deserialize_json(data: str) -> IncludeOptions:
    return cast(IncludeOptions, data)
