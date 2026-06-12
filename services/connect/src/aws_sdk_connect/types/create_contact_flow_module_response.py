"""Generated from Smithy shape ``com.amazonaws.connect#CreateContactFlowModuleResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.contact_flow_module_id


class CreateContactFlowModuleResponse(TypedDict):
    id: NotRequired["aws_sdk_connect.types.contact_flow_module_id.ContactFlowModuleId"]
    """<p>The identifier of the flow module.</p>"""
    arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the flow module.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateContactFlowModuleResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> CreateContactFlowModuleResponse:
    out: CreateContactFlowModuleResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
