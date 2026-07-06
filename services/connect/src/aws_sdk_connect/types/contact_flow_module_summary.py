"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowModuleSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.contact_flow_module_id
    import aws_sdk_connect.types.contact_flow_module_name
    import aws_sdk_connect.types.contact_flow_module_state


class ContactFlowModuleSummary(TypedDict, closed=True):
    id: NotRequired["aws_sdk_connect.types.contact_flow_module_id.ContactFlowModuleId"]
    """<p>The identifier of the flow module.</p>"""
    arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the flow module.</p>"""
    name: NotRequired[
        "aws_sdk_connect.types.contact_flow_module_name.ContactFlowModuleName"
    ]
    """<p>The name of the flow module.</p>"""
    state: NotRequired[
        "aws_sdk_connect.types.contact_flow_module_state.ContactFlowModuleState"
    ]
    """<p>The type of flow module.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowModuleSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "state" in value:
        import aws_sdk_connect.types.contact_flow_module_state

        out["State"] = aws_sdk_connect.types.contact_flow_module_state.serialize_json(
            value["state"]
        )
    return out


def deserialize_json(data: dict) -> ContactFlowModuleSummary:
    out: ContactFlowModuleSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "State" in data:
        import aws_sdk_connect.types.contact_flow_module_state

        out["state"] = aws_sdk_connect.types.contact_flow_module_state.deserialize_json(
            data["State"]
        )
    return out
