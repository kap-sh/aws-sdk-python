"""Generated from Smithy shape ``com.amazonaws.connect#DescribeAttachedFilesConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.attachment_scope
    import aws_sdk_connect.types.instance_id


class DescribeAttachedFilesConfigurationRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    attachment_scope: "aws_sdk_connect.types.attachment_scope.AttachmentScope"
    """<p>The scope of the attachment. Valid values are <code>EMAIL</code>, <code>CHAT</code>, <code>CASE</code>, and <code>TASK</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAttachedFilesConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAttachedFilesConfigurationRequest:
    out: DescribeAttachedFilesConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
