"""Generated from Smithy shape ``com.amazonaws.panorama#NodeSignal``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_panorama.types.node_instance_id
    import aws_sdk_panorama.types.node_signal_value


class NodeSignal(TypedDict, closed=True):
    node_instance_id: "aws_sdk_panorama.types.node_instance_id.NodeInstanceId"
    """<p>The camera node's name, from the application manifest.</p>"""
    signal: "aws_sdk_panorama.types.node_signal_value.NodeSignalValue"
    """<p>The signal value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeSignal) -> dict:
    out: dict = {}
    out["NodeInstanceId"] = value["node_instance_id"]
    out["Signal"] = value["signal"]
    return out


def deserialize_json(data: dict) -> NodeSignal:
    out: NodeSignal = {}  # type: ignore[typeddict-item]
    if "NodeInstanceId" in data:
        out["node_instance_id"] = data["NodeInstanceId"]
    else:
        raise DeserializationError("NodeSignal.node_instance_id required")
    if "Signal" in data:
        out["signal"] = data["Signal"]
    else:
        raise DeserializationError("NodeSignal.signal required")
    return out
