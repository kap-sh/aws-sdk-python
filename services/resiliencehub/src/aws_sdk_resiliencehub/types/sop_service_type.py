"""Generated from Smithy shape ``com.amazonaws.resiliencehub#SopServiceType``."""

from typing import Literal, TypeAlias, cast

SopServiceType: TypeAlias = Literal["SSM",]


# --- restJson1 ser/de ---
def serialize_json(value: SopServiceType) -> str:
    return value


def deserialize_json(data: str) -> SopServiceType:
    return cast(SopServiceType, data)
