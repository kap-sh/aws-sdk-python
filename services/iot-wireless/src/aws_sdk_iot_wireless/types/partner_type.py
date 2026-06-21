"""Generated from Smithy shape ``com.amazonaws.iotwireless#PartnerType``."""

from typing import Literal, TypeAlias, cast

PartnerType: TypeAlias = Literal["Sidewalk",]


# --- restJson1 ser/de ---
def serialize_json(value: PartnerType) -> str:
    return value


def deserialize_json(data: str) -> PartnerType:
    return cast(PartnerType, data)
