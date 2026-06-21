"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#ObfuscationSetting``."""

from typing import Literal, TypeAlias, cast

ObfuscationSetting: TypeAlias = Literal[
    "NONE",
    "DEFAULT_OBFUSCATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: ObfuscationSetting) -> str:
    return value


def deserialize_json(data: str) -> ObfuscationSetting:
    return cast(ObfuscationSetting, data)
