"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfOutput``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconvert.types.output

__listOfOutput: TypeAlias = list["capo_mediaconvert.types.output.Output"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfOutput) -> list:
    import capo_mediaconvert.types.output

    out: list = []
    for item in value:
        out.append(capo_mediaconvert.types.output.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfOutput:
    import capo_mediaconvert.types.output

    out: __listOfOutput = []
    for item in data:
        out.append(capo_mediaconvert.types.output.deserialize_json(item))
    return out
