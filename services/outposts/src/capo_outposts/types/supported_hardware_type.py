"""Generated from Smithy shape ``com.amazonaws.outposts#SupportedHardwareType``."""

from typing import Literal, TypeAlias, cast

SupportedHardwareType: TypeAlias = Literal[
    "RACK",
    "SERVER",
]


# --- restJson1 ser/de ---
def serialize_json(value: SupportedHardwareType) -> str:
    return value


def deserialize_json(data: str) -> SupportedHardwareType:
    return cast(SupportedHardwareType, data)
