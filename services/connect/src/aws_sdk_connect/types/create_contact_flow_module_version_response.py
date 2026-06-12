"""Generated from Smithy shape ``com.amazonaws.connect#CreateContactFlowModuleVersionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.resource_version


class CreateContactFlowModuleVersionResponse(TypedDict):
    contact_flow_module_arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the flow module.</p>"""
    version: NotRequired["aws_sdk_connect.types.resource_version.ResourceVersion"]
    """<p>The version of the flow module.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateContactFlowModuleVersionResponse) -> dict:
    out: dict = {}
    if "contact_flow_module_arn" in value:
        out["ContactFlowModuleArn"] = value["contact_flow_module_arn"]
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_json(data: dict) -> CreateContactFlowModuleVersionResponse:
    out: CreateContactFlowModuleVersionResponse = {}  # type: ignore[typeddict-item]
    if "ContactFlowModuleArn" in data:
        out["contact_flow_module_arn"] = data["ContactFlowModuleArn"]
    if "Version" in data:
        out["version"] = data["Version"]
    return out
