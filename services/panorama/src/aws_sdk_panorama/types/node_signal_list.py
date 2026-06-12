"""Generated from Smithy shape ``com.amazonaws.panorama#NodeSignalList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_panorama.types.node_signal

NodeSignalList: TypeAlias = list["aws_sdk_panorama.types.node_signal.NodeSignal"]


# --- restJson1 ser/de ---
def serialize_json(value: NodeSignalList) -> list:
    import aws_sdk_panorama.types.node_signal

    out: list = []
    for item in value:
        out.append(aws_sdk_panorama.types.node_signal.serialize_json(item))
    return out


def deserialize_json(data: list) -> NodeSignalList:
    import aws_sdk_panorama.types.node_signal

    out: NodeSignalList = []
    for item in data:
        out.append(aws_sdk_panorama.types.node_signal.deserialize_json(item))
    return out
