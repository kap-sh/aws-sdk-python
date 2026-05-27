"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedLogGroup``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.managed_resource_status
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class ManagedLogGroup(TypedDict):
    arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Cloudwatch Log Group associated with the Express service.</p>"""
    status: "aws_sdk_ecs.types.managed_resource_status.ManagedResourceStatus"
    """<p>The status of the Cloudwatch LogGroup.</p>"""
    status_reason: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>Information about why the Cloudwatch LogGroup is in the current status.</p>"""
    updated_at: "aws_sdk_ecs.types.timestamp.Timestamp"
    """<p>The Unix timestamp for when the Cloudwatch LogGroup was last updated</p>"""
    log_group_name: "aws_sdk_ecs.types.string.String"
    """<p>The name of the Cloudwatch Log Group associated with the Express service.</p>"""
