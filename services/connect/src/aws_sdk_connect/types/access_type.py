"""Generated from Smithy shape ``com.amazonaws.connect#AccessType``."""

from typing import Literal, TypeAlias, cast

AccessType: TypeAlias = Literal["ALLOW",]


# --- restJson1 ser/de ---
def serialize_json(value: AccessType) -> str:
    return value


def deserialize_json(data: str) -> AccessType:
    return cast(AccessType, data)
