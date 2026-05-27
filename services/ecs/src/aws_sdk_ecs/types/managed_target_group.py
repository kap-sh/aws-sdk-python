"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedTargetGroup``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.integer
    import aws_sdk_ecs.types.managed_resource_status
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class ManagedTargetGroup(TypedDict):
    arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the target group.</p>"""
    status: "aws_sdk_ecs.types.managed_resource_status.ManagedResourceStatus"
    """<p>The status of the target group.</p>"""
    status_reason: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>Information about why the target group is in the current status.</p>"""
    updated_at: "aws_sdk_ecs.types.timestamp.Timestamp"
    """<p>The Unix timestamp for when the target group was last updated.</p>"""
    health_check_path: "aws_sdk_ecs.types.string.String"
    """<p>The destination for health checks on the targets.</p>"""
    health_check_port: "aws_sdk_ecs.types.integer.Integer"
    """<p>The port the load balancer uses when performing health checks on targets.</p>"""
    port: "aws_sdk_ecs.types.integer.Integer"
    """<p>The port on which the targets receive traffic.</p>"""
