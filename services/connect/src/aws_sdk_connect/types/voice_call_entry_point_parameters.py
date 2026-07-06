"""Generated from Smithy shape ``com.amazonaws.connect#VoiceCallEntryPointParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_flow_id
    import aws_sdk_connect.types.phone_number


class VoiceCallEntryPointParameters(TypedDict, closed=True):
    source_phone_number: NotRequired["aws_sdk_connect.types.phone_number.PhoneNumber"]
    """<p>The source phone number for the test.</p>"""
    destination_phone_number: NotRequired[
        "aws_sdk_connect.types.phone_number.PhoneNumber"
    ]
    """<p>The destination phone number for the test.</p>"""
    flow_id: NotRequired["aws_sdk_connect.types.contact_flow_id.ContactFlowId"]
    """<p>The flow identifier for the test.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VoiceCallEntryPointParameters) -> dict:
    out: dict = {}
    if "source_phone_number" in value:
        out["SourcePhoneNumber"] = value["source_phone_number"]
    if "destination_phone_number" in value:
        out["DestinationPhoneNumber"] = value["destination_phone_number"]
    if "flow_id" in value:
        out["FlowId"] = value["flow_id"]
    return out


def deserialize_json(data: dict) -> VoiceCallEntryPointParameters:
    out: VoiceCallEntryPointParameters = {}  # type: ignore[typeddict-item]
    if "SourcePhoneNumber" in data:
        out["source_phone_number"] = data["SourcePhoneNumber"]
    if "DestinationPhoneNumber" in data:
        out["destination_phone_number"] = data["DestinationPhoneNumber"]
    if "FlowId" in data:
        out["flow_id"] = data["FlowId"]
    return out
