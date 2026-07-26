"""Generated from Smithy shape ``com.amazonaws.groundstation#DataflowEndpointGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_groundstation.types.dataflow_endpoint_list_item

DataflowEndpointGroupList: TypeAlias = list[
    "capo_groundstation.types.dataflow_endpoint_list_item.DataflowEndpointListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataflowEndpointGroupList) -> list:
    import capo_groundstation.types.dataflow_endpoint_list_item

    out: list = []
    for item in value:
        out.append(
            capo_groundstation.types.dataflow_endpoint_list_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DataflowEndpointGroupList:
    import capo_groundstation.types.dataflow_endpoint_list_item

    out: DataflowEndpointGroupList = []
    for item in data:
        out.append(
            capo_groundstation.types.dataflow_endpoint_list_item.deserialize_json(item)
        )
    return out
