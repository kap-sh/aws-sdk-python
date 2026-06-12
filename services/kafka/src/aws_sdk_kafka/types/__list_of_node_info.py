"""Generated from Smithy shape ``com.amazonaws.kafka#__listOfNodeInfo``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kafka.types.node_info

__listOfNodeInfo: TypeAlias = list["aws_sdk_kafka.types.node_info.NodeInfo"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfNodeInfo) -> list:
    import aws_sdk_kafka.types.node_info

    out: list = []
    for item in value:
        out.append(aws_sdk_kafka.types.node_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfNodeInfo:
    import aws_sdk_kafka.types.node_info

    out: __listOfNodeInfo = []
    for item in data:
        out.append(aws_sdk_kafka.types.node_info.deserialize_json(item))
    return out
