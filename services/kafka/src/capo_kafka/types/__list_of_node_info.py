"""Generated from Smithy shape ``com.amazonaws.kafka#__listOfNodeInfo``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kafka.types.node_info

__listOfNodeInfo: TypeAlias = list["capo_kafka.types.node_info.NodeInfo"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfNodeInfo) -> list:
    import capo_kafka.types.node_info

    out: list = []
    for item in value:
        out.append(capo_kafka.types.node_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfNodeInfo:
    import capo_kafka.types.node_info

    out: __listOfNodeInfo = []
    for item in data:
        out.append(capo_kafka.types.node_info.deserialize_json(item))
    return out
