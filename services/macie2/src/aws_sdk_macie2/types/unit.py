"""Generated from Smithy shape ``com.amazonaws.macie2#Unit``."""

from typing import Literal, TypeAlias, cast

Unit: TypeAlias = Literal["TERABYTES",]


# --- restJson1 ser/de ---
def serialize_json(value: Unit) -> str:
    return value


def deserialize_json(data: str) -> Unit:
    return cast(Unit, data)
