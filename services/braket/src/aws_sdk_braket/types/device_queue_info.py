"""Generated from Smithy shape ``com.amazonaws.braket#DeviceQueueInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_braket.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_braket.types.queue_name
    import aws_sdk_braket.types.queue_priority

class DeviceQueueInfo(TypedDict):
    queue: "aws_sdk_braket.types.queue_name.QueueName"
    """<p>The name of the queue. </p>"""
    queue_size: "str"
    """<p>The number of hybrid jobs or quantum tasks in the queue for a given device. </p>"""
    queue_priority: NotRequired["aws_sdk_braket.types.queue_priority.QueuePriority"]
    """<p>Optional. Specifies the priority of the queue. Quantum tasks in a priority queue are processed before the quantum tasks in a normal queue.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeviceQueueInfo) -> dict:
    out: dict = {}
    out["queue"] = value["queue"]
    out["queueSize"] = value["queue_size"]
    if "queue_priority" in value:
        out["queuePriority"] = value["queue_priority"]
    return out


def deserialize_json(data: dict) -> DeviceQueueInfo:
    out: DeviceQueueInfo = {}  # type: ignore[typeddict-item]
    if "queue" in data:
        out["queue"] = data["queue"]
    else:
        raise DeserializationError("DeviceQueueInfo.queue required")
    if "queueSize" in data:
        out["queue_size"] = data["queueSize"]
    else:
        raise DeserializationError("DeviceQueueInfo.queue_size required")
    if "queuePriority" in data:
        out["queue_priority"] = data["queuePriority"]
    return out