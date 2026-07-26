"""Generated from Smithy shape ``com.amazonaws.mediaconvert#WatermarkingStrength``."""

from typing import Literal, TypeAlias, cast

"""Optional. Ignore this setting unless Nagra support directs you to specify a value. When you don't specify a value here, the Nagra NexGuard library uses its default value."""
WatermarkingStrength: TypeAlias = Literal[
    "LIGHTEST",
    "LIGHTER",
    "DEFAULT",
    "STRONGER",
    "STRONGEST",
]


# --- restJson1 ser/de ---
def serialize_json(value: WatermarkingStrength) -> str:
    return value


def deserialize_json(data: str) -> WatermarkingStrength:
    return cast(WatermarkingStrength, data)
