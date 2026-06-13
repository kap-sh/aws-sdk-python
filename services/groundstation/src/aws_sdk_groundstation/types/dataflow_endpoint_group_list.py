"""Generated from Smithy shape ``com.amazonaws.groundstation#DataflowEndpointGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.dataflow_endpoint_list_item

DataflowEndpointGroupList: TypeAlias = list[
    "aws_sdk_groundstation.types.dataflow_endpoint_list_item.DataflowEndpointListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataflowEndpointGroupList) -> list:
    import aws_sdk_groundstation.types.dataflow_endpoint_list_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_groundstation.types.dataflow_endpoint_list_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DataflowEndpointGroupList:
    import aws_sdk_groundstation.types.dataflow_endpoint_list_item

    out: DataflowEndpointGroupList = []
    for item in data:
        out.append(
            aws_sdk_groundstation.types.dataflow_endpoint_list_item.deserialize_json(
                item
            )
        )
    return out
