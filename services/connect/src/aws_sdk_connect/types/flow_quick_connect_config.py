"""Generated from Smithy shape ``com.amazonaws.connect#FlowQuickConnectConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_flow_id


class FlowQuickConnectConfig(TypedDict):
    contact_flow_id: "aws_sdk_connect.types.contact_flow_id.ContactFlowId"
    """<p> The contact flow ID for the quick connect configuration. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowQuickConnectConfig) -> dict:
    out: dict = {}
    out["ContactFlowId"] = value["contact_flow_id"]
    return out


def deserialize_json(data: dict) -> FlowQuickConnectConfig:
    out: FlowQuickConnectConfig = {}  # type: ignore[typeddict-item]
    if "ContactFlowId" in data:
        out["contact_flow_id"] = data["ContactFlowId"]
    else:
        raise DeserializationError("FlowQuickConnectConfig.contact_flow_id required")
    return out
