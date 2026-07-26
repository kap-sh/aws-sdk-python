"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfOutputGroup``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconvert.types.output_group

__listOfOutputGroup: TypeAlias = list[
    "capo_mediaconvert.types.output_group.OutputGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfOutputGroup) -> list:
    import capo_mediaconvert.types.output_group

    out: list = []
    for item in value:
        out.append(capo_mediaconvert.types.output_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfOutputGroup:
    import capo_mediaconvert.types.output_group

    out: __listOfOutputGroup = []
    for item in data:
        out.append(capo_mediaconvert.types.output_group.deserialize_json(item))
    return out
