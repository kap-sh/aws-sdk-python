"""Generated from Smithy shape ``com.amazonaws.mediaconvert#FileSourceTimeDeltaUnits``."""

from typing import Literal, TypeAlias, cast

"""When you use the setting Time delta to adjust the sync between your sidecar captions and your video, use this setting to specify the units for the delta that you specify. When you don't specify a value for Time delta units, MediaConvert uses seconds by default."""
FileSourceTimeDeltaUnits: TypeAlias = Literal[
    "SECONDS",
    "MILLISECONDS",
]


# --- restJson1 ser/de ---
def serialize_json(value: FileSourceTimeDeltaUnits) -> str:
    return value


def deserialize_json(data: str) -> FileSourceTimeDeltaUnits:
    return cast(FileSourceTimeDeltaUnits, data)
