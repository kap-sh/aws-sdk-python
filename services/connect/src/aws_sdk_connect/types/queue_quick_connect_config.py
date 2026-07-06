"""Generated from Smithy shape ``com.amazonaws.connect#QueueQuickConnectConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_flow_id
    import aws_sdk_connect.types.queue_id


class QueueQuickConnectConfig(TypedDict, closed=True):
    queue_id: "aws_sdk_connect.types.queue_id.QueueId"
    """<p>The identifier for the queue.</p>"""
    contact_flow_id: "aws_sdk_connect.types.contact_flow_id.ContactFlowId"
    """<p>The identifier of the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueueQuickConnectConfig) -> dict:
    out: dict = {}
    out["QueueId"] = value["queue_id"]
    out["ContactFlowId"] = value["contact_flow_id"]
    return out


def deserialize_json(data: dict) -> QueueQuickConnectConfig:
    out: QueueQuickConnectConfig = {}  # type: ignore[typeddict-item]
    if "QueueId" in data:
        out["queue_id"] = data["QueueId"]
    else:
        raise DeserializationError("QueueQuickConnectConfig.queue_id required")
    if "ContactFlowId" in data:
        out["contact_flow_id"] = data["ContactFlowId"]
    else:
        raise DeserializationError("QueueQuickConnectConfig.contact_flow_id required")
    return out
