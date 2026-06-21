"""Generated from Smithy shape ``com.amazonaws.mediaconvert#PresetListBy``."""

from typing import Literal, TypeAlias, cast

"""Optional. When you request a list of presets, you can choose to list them alphabetically by NAME or chronologically by CREATION_DATE. If you don't specify, the service will list them by name."""
PresetListBy: TypeAlias = Literal[
    "NAME",
    "CREATION_DATE",
    "SYSTEM",
]


# --- restJson1 ser/de ---
def serialize_json(value: PresetListBy) -> str:
    return value


def deserialize_json(data: str) -> PresetListBy:
    return cast(PresetListBy, data)
