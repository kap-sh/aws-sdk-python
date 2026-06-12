"""Generated from Smithy shape ``com.amazonaws.connect#CreateContactFlowResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.contact_flow_id
    import aws_sdk_connect.types.flow_content_sha256


class CreateContactFlowResponse(TypedDict):
    contact_flow_id: NotRequired["aws_sdk_connect.types.contact_flow_id.ContactFlowId"]
    """<p>The identifier of the flow.</p>"""
    contact_flow_arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the flow.</p>"""
    flow_content_sha256: NotRequired[
        "aws_sdk_connect.types.flow_content_sha256.FlowContentSha256"
    ]
    """<p>Indicates the checksum value of the latest published flow content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateContactFlowResponse) -> dict:
    out: dict = {}
    if "contact_flow_id" in value:
        out["ContactFlowId"] = value["contact_flow_id"]
    if "contact_flow_arn" in value:
        out["ContactFlowArn"] = value["contact_flow_arn"]
    if "flow_content_sha256" in value:
        out["FlowContentSha256"] = value["flow_content_sha256"]
    return out


def deserialize_json(data: dict) -> CreateContactFlowResponse:
    out: CreateContactFlowResponse = {}  # type: ignore[typeddict-item]
    if "ContactFlowId" in data:
        out["contact_flow_id"] = data["ContactFlowId"]
    if "ContactFlowArn" in data:
        out["contact_flow_arn"] = data["ContactFlowArn"]
    if "FlowContentSha256" in data:
        out["flow_content_sha256"] = data["FlowContentSha256"]
    return out
