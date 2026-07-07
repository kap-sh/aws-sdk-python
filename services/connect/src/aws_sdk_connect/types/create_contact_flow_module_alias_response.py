"""Generated from Smithy shape ``com.amazonaws.connect#CreateContactFlowModuleAliasResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.resource_id


class CreateContactFlowModuleAliasResponse(TypedDict, closed=True):
    contact_flow_module_arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the flow module.</p>"""
    id: NotRequired["aws_sdk_connect.types.resource_id.ResourceId"]
    """<p>The identifier of the alias.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateContactFlowModuleAliasResponse) -> dict:
    out: dict = {}
    if "contact_flow_module_arn" in value:
        out["ContactFlowModuleArn"] = value["contact_flow_module_arn"]
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> CreateContactFlowModuleAliasResponse:
    out: CreateContactFlowModuleAliasResponse = {}  # type: ignore[typeddict-item]
    if "ContactFlowModuleArn" in data:
        out["contact_flow_module_arn"] = data["ContactFlowModuleArn"]
    if "Id" in data:
        out["id"] = data["Id"]
    return out
