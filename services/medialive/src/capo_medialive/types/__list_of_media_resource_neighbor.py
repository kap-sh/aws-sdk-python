"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfMediaResourceNeighbor``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.media_resource_neighbor

__listOfMediaResourceNeighbor: TypeAlias = list[
    "capo_medialive.types.media_resource_neighbor.MediaResourceNeighbor"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfMediaResourceNeighbor) -> list:
    import capo_medialive.types.media_resource_neighbor

    out: list = []
    for item in value:
        out.append(capo_medialive.types.media_resource_neighbor.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfMediaResourceNeighbor:
    import capo_medialive.types.media_resource_neighbor

    out: __listOfMediaResourceNeighbor = []
    for item in data:
        out.append(capo_medialive.types.media_resource_neighbor.deserialize_json(item))
    return out
