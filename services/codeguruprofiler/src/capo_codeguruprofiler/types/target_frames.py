"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#TargetFrames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.target_frame

TargetFrames: TypeAlias = list["capo_codeguruprofiler.types.target_frame.TargetFrame"]


# --- restJson1 ser/de ---
def serialize_json(value: TargetFrames) -> list:
    import capo_codeguruprofiler.types.target_frame

    out: list = []
    for item in value:
        out.append(capo_codeguruprofiler.types.target_frame.serialize_json(item))
    return out


def deserialize_json(data: list) -> TargetFrames:
    import capo_codeguruprofiler.types.target_frame

    out: TargetFrames = []
    for item in data:
        out.append(capo_codeguruprofiler.types.target_frame.deserialize_json(item))
    return out
