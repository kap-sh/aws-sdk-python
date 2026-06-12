"""Generated from Smithy shape ``com.amazonaws.connect#ChatEntryPointParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_flow_id


class ChatEntryPointParameters(TypedDict):
    flow_id: NotRequired["aws_sdk_connect.types.contact_flow_id.ContactFlowId"]
    """<p>The flow identifier for the test.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChatEntryPointParameters) -> dict:
    out: dict = {}
    if "flow_id" in value:
        out["FlowId"] = value["flow_id"]
    return out


def deserialize_json(data: dict) -> ChatEntryPointParameters:
    out: ChatEntryPointParameters = {}  # type: ignore[typeddict-item]
    if "FlowId" in data:
        out["flow_id"] = data["FlowId"]
    return out
