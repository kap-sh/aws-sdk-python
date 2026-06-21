"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#FixedPosition``."""

from typing import Literal, TypeAlias, cast

FixedPosition: TypeAlias = Literal["first",]


# --- restJson1 ser/de ---
def serialize_json(value: FixedPosition) -> str:
    return value


def deserialize_json(data: str) -> FixedPosition:
    return cast(FixedPosition, data)
