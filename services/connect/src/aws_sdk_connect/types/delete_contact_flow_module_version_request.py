"""Generated from Smithy shape ``com.amazonaws.connect#DeleteContactFlowModuleVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.resource_version


class DeleteContactFlowModuleVersionRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_flow_module_id: "aws_sdk_connect.types.arn.ARN"
    """<p>The identifier of the flow module.</p>"""
    contact_flow_module_version: (
        "aws_sdk_connect.types.resource_version.ResourceVersion"
    )
    """<p>The version of the flow module to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteContactFlowModuleVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteContactFlowModuleVersionRequest:
    out: DeleteContactFlowModuleVersionRequest = {}  # type: ignore[typeddict-item]
    return out
