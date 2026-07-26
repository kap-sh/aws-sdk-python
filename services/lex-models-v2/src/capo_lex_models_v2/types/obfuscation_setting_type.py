"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ObfuscationSettingType``."""

from typing import Literal, TypeAlias, cast

ObfuscationSettingType: TypeAlias = Literal[
    "None",
    "DefaultObfuscation",
]


# --- restJson1 ser/de ---
def serialize_json(value: ObfuscationSettingType) -> str:
    return value


def deserialize_json(data: str) -> ObfuscationSettingType:
    return cast(ObfuscationSettingType, data)
