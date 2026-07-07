"""Generated from Smithy shape ``com.amazonaws.connect#OutboundCallerConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_flow_id
    import aws_sdk_connect.types.outbound_caller_id_name
    import aws_sdk_connect.types.phone_number_id


class OutboundCallerConfig(TypedDict, closed=True):
    outbound_caller_id_name: NotRequired[
        "aws_sdk_connect.types.outbound_caller_id_name.OutboundCallerIdName"
    ]
    """<p>The caller ID name.</p>"""
    outbound_caller_id_number_id: NotRequired[
        "aws_sdk_connect.types.phone_number_id.PhoneNumberId"
    ]
    """<p>The caller ID number.</p>"""
    outbound_flow_id: NotRequired["aws_sdk_connect.types.contact_flow_id.ContactFlowId"]
    """<p>The outbound whisper flow to be used during an outbound call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutboundCallerConfig) -> dict:
    out: dict = {}
    if "outbound_caller_id_name" in value:
        out["OutboundCallerIdName"] = value["outbound_caller_id_name"]
    if "outbound_caller_id_number_id" in value:
        out["OutboundCallerIdNumberId"] = value["outbound_caller_id_number_id"]
    if "outbound_flow_id" in value:
        out["OutboundFlowId"] = value["outbound_flow_id"]
    return out


def deserialize_json(data: dict) -> OutboundCallerConfig:
    out: OutboundCallerConfig = {}  # type: ignore[typeddict-item]
    if "OutboundCallerIdName" in data:
        out["outbound_caller_id_name"] = data["OutboundCallerIdName"]
    if "OutboundCallerIdNumberId" in data:
        out["outbound_caller_id_number_id"] = data["OutboundCallerIdNumberId"]
    if "OutboundFlowId" in data:
        out["outbound_flow_id"] = data["OutboundFlowId"]
    return out
