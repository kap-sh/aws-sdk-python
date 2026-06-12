"""Generated from Smithy shape ``com.amazonaws.connect#CreateContactFlowVersionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.resource_version


class CreateContactFlowVersionResponse(TypedDict):
    contact_flow_arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the flow.</p>"""
    version: NotRequired["aws_sdk_connect.types.resource_version.ResourceVersion"]
    """<p>The identifier of the flow version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateContactFlowVersionResponse) -> dict:
    out: dict = {}
    if "contact_flow_arn" in value:
        out["ContactFlowArn"] = value["contact_flow_arn"]
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_json(data: dict) -> CreateContactFlowVersionResponse:
    out: CreateContactFlowVersionResponse = {}  # type: ignore[typeddict-item]
    if "ContactFlowArn" in data:
        out["contact_flow_arn"] = data["ContactFlowArn"]
    if "Version" in data:
        out["version"] = data["Version"]
    return out
