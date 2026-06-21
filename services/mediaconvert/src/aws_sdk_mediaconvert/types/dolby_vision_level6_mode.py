"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DolbyVisionLevel6Mode``."""

from typing import Literal, TypeAlias, cast

"""Use Dolby Vision Mode to choose how the service will handle Dolby Vision MaxCLL and MaxFALL properies."""
DolbyVisionLevel6Mode: TypeAlias = Literal[
    "PASSTHROUGH",
    "RECALCULATE",
    "SPECIFY",
]


# --- restJson1 ser/de ---
def serialize_json(value: DolbyVisionLevel6Mode) -> str:
    return value


def deserialize_json(data: str) -> DolbyVisionLevel6Mode:
    return cast(DolbyVisionLevel6Mode, data)
