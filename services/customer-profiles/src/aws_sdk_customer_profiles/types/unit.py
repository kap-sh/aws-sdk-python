"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Unit``."""

from typing import Literal, TypeAlias, cast

Unit: TypeAlias = Literal["DAYS",]


# --- restJson1 ser/de ---
def serialize_json(value: Unit) -> str:
    return value


def deserialize_json(data: str) -> Unit:
    return cast(Unit, data)
