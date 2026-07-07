"""Generated from Smithy shape ``com.amazonaws.connect#DeleteContactFlowVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.resource_version


class DeleteContactFlowVersionRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_flow_id: "aws_sdk_connect.types.arn.ARN"
    """<p>The identifier of the flow.</p>"""
    contact_flow_version: "aws_sdk_connect.types.resource_version.ResourceVersion"
    """<p>The identifier of the flow version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteContactFlowVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteContactFlowVersionRequest:
    out: DeleteContactFlowVersionRequest = {}  # type: ignore[typeddict-item]
    return out
