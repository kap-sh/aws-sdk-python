"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#ResourceEndpointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.resource_endpoint_list_item

ResourceEndpointList: TypeAlias = list[
    "aws_sdk_kinesis_video.types.resource_endpoint_list_item.ResourceEndpointListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceEndpointList) -> list:
    import aws_sdk_kinesis_video.types.resource_endpoint_list_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kinesis_video.types.resource_endpoint_list_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ResourceEndpointList:
    import aws_sdk_kinesis_video.types.resource_endpoint_list_item

    out: ResourceEndpointList = []
    for item in data:
        out.append(
            aws_sdk_kinesis_video.types.resource_endpoint_list_item.deserialize_json(
                item
            )
        )
    return out
