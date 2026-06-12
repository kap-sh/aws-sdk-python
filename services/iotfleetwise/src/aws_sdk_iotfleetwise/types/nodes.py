"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#Nodes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.node

Nodes: TypeAlias = list["aws_sdk_iotfleetwise.types.node.Node"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Nodes) -> list:
    import aws_sdk_iotfleetwise.types.node

    out: list = []
    for item in value:
        out.append(aws_sdk_iotfleetwise.types.node.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Nodes:
    import aws_sdk_iotfleetwise.types.node

    out: Nodes = []
    for item in data:
        out.append(aws_sdk_iotfleetwise.types.node.deserialize_aws_json_1_0(item))
    return out
