"""Generated from Smithy shape ``com.amazonaws.imagebuilder#TenancyType``."""

from typing import Literal, TypeAlias, cast

TenancyType: TypeAlias = Literal[
    "default",
    "dedicated",
    "host",
]


# --- restJson1 ser/de ---
def serialize_json(value: TenancyType) -> str:
    return value


def deserialize_json(data: str) -> TenancyType:
    return cast(TenancyType, data)
