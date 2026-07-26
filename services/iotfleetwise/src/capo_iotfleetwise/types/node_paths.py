"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#NodePaths``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotfleetwise.types.node_path

NodePaths: TypeAlias = list["capo_iotfleetwise.types.node_path.NodePath"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NodePaths) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> NodePaths:
    return list(data)
