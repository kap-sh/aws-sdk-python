"""Generated from Smithy shape ``com.amazonaws.connect#UpdateContactFlowModuleContentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_flow_module_content
    import aws_sdk_connect.types.contact_flow_module_id
    import aws_sdk_connect.types.flow_module_settings
    import aws_sdk_connect.types.instance_id


class UpdateContactFlowModuleContentRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_flow_module_id: (
        "aws_sdk_connect.types.contact_flow_module_id.ContactFlowModuleId"
    )
    """<p>The identifier of the flow module.</p>"""
    content: NotRequired[
        "aws_sdk_connect.types.contact_flow_module_content.ContactFlowModuleContent"
    ]
    r"""<p>The JSON string that represents the content of the flow. For an example, see <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/flow-language-example.html\">Example flow in Connect Customer Flow language</a>. </p>"""
    settings: NotRequired[
        "aws_sdk_connect.types.flow_module_settings.FlowModuleSettings"
    ]
    """<p>Serialized JSON string of the flow module Settings schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateContactFlowModuleContentRequest) -> dict:
    out: dict = {}
    if "content" in value:
        out["Content"] = value["content"]
    if "settings" in value:
        out["Settings"] = value["settings"]
    return out


def deserialize_json(data: dict) -> UpdateContactFlowModuleContentRequest:
    out: UpdateContactFlowModuleContentRequest = {}  # type: ignore[typeddict-item]
    if "Content" in data:
        out["content"] = data["Content"]
    if "Settings" in data:
        out["settings"] = data["Settings"]
    return out
