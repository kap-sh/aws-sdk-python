"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfMulticastSource``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.multicast_source

__listOfMulticastSource: TypeAlias = list[
    "capo_medialive.types.multicast_source.MulticastSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfMulticastSource) -> list:
    import capo_medialive.types.multicast_source

    out: list = []
    for item in value:
        out.append(capo_medialive.types.multicast_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfMulticastSource:
    import capo_medialive.types.multicast_source

    out: __listOfMulticastSource = []
    for item in data:
        out.append(capo_medialive.types.multicast_source.deserialize_json(item))
    return out
