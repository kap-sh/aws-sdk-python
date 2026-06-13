"""Generated from Smithy shape ``com.amazonaws.braket#HybridJobQueueInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_braket.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_braket.types.queue_name


class HybridJobQueueInfo(TypedDict):
    queue: "aws_sdk_braket.types.queue_name.QueueName"
    """<p>The name of the queue.</p>"""
    position: "str"
    """<p>Current position of the hybrid job in the jobs queue.</p>"""
    message: NotRequired["str"]
    """<p>Optional. Provides more information about the queue position. For example, if the hybrid job is complete and no longer in the queue, the message field contains that information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HybridJobQueueInfo) -> dict:
    out: dict = {}
    out["queue"] = value["queue"]
    out["position"] = value["position"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> HybridJobQueueInfo:
    out: HybridJobQueueInfo = {}  # type: ignore[typeddict-item]
    if "queue" in data:
        out["queue"] = data["queue"]
    else:
        raise DeserializationError("HybridJobQueueInfo.queue required")
    if "position" in data:
        out["position"] = data["position"]
    else:
        raise DeserializationError("HybridJobQueueInfo.position required")
    if "message" in data:
        out["message"] = data["message"]
    return out
