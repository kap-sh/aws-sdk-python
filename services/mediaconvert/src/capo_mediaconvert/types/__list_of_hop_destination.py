"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfHopDestination``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconvert.types.hop_destination

__listOfHopDestination: TypeAlias = list[
    "capo_mediaconvert.types.hop_destination.HopDestination"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfHopDestination) -> list:
    import capo_mediaconvert.types.hop_destination

    out: list = []
    for item in value:
        out.append(capo_mediaconvert.types.hop_destination.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfHopDestination:
    import capo_mediaconvert.types.hop_destination

    out: __listOfHopDestination = []
    for item in data:
        out.append(capo_mediaconvert.types.hop_destination.deserialize_json(item))
    return out
