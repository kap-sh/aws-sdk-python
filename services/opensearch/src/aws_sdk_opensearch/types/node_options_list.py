"""Generated from Smithy shape ``com.amazonaws.opensearch#NodeOptionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.node_option

NodeOptionsList: TypeAlias = list["aws_sdk_opensearch.types.node_option.NodeOption"]


# --- restJson1 ser/de ---
def serialize_json(value: NodeOptionsList) -> list:
    import aws_sdk_opensearch.types.node_option

    out: list = []
    for item in value:
        out.append(aws_sdk_opensearch.types.node_option.serialize_json(item))
    return out


def deserialize_json(data: list) -> NodeOptionsList:
    import aws_sdk_opensearch.types.node_option

    out: NodeOptionsList = []
    for item in data:
        out.append(aws_sdk_opensearch.types.node_option.deserialize_json(item))
    return out
