"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#ResourceEndpointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis_video.types.resource_endpoint_list_item

ResourceEndpointList: TypeAlias = list[
    "capo_kinesis_video.types.resource_endpoint_list_item.ResourceEndpointListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceEndpointList) -> list:
    import capo_kinesis_video.types.resource_endpoint_list_item

    out: list = []
    for item in value:
        out.append(
            capo_kinesis_video.types.resource_endpoint_list_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ResourceEndpointList:
    import capo_kinesis_video.types.resource_endpoint_list_item

    out: ResourceEndpointList = []
    for item in data:
        out.append(
            capo_kinesis_video.types.resource_endpoint_list_item.deserialize_json(item)
        )
    return out
