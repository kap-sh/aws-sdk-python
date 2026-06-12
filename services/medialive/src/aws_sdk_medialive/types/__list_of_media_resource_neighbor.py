"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfMediaResourceNeighbor``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.media_resource_neighbor

__listOfMediaResourceNeighbor: TypeAlias = list[
    "aws_sdk_medialive.types.media_resource_neighbor.MediaResourceNeighbor"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfMediaResourceNeighbor) -> list:
    import aws_sdk_medialive.types.media_resource_neighbor

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.media_resource_neighbor.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfMediaResourceNeighbor:
    import aws_sdk_medialive.types.media_resource_neighbor

    out: __listOfMediaResourceNeighbor = []
    for item in data:
        out.append(
            aws_sdk_medialive.types.media_resource_neighbor.deserialize_json(item)
        )
    return out
