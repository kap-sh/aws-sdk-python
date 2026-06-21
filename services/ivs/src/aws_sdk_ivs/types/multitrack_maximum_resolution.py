"""Generated from Smithy shape ``com.amazonaws.ivs#MultitrackMaximumResolution``."""

from typing import Literal, TypeAlias, cast

MultitrackMaximumResolution: TypeAlias = Literal[
    "SD",
    "HD",
    "FULL_HD",
]


# --- restJson1 ser/de ---
def serialize_json(value: MultitrackMaximumResolution) -> str:
    return value


def deserialize_json(data: str) -> MultitrackMaximumResolution:
    return cast(MultitrackMaximumResolution, data)
