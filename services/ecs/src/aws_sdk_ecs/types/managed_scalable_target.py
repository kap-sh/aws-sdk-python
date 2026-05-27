"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedScalableTarget``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.integer
    import aws_sdk_ecs.types.managed_resource_status
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.timestamp


class ManagedScalableTarget(TypedDict):
    arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the scalable target.</p>"""
    status: "aws_sdk_ecs.types.managed_resource_status.ManagedResourceStatus"
    """<p>The status of the scalable target.</p>"""
    status_reason: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>Information about why the scalable target is in the current status.</p>"""
    updated_at: "aws_sdk_ecs.types.timestamp.Timestamp"
    """<p>The Unix timestamp for when the target was most recently updated.</p>"""
    min_capacity: "aws_sdk_ecs.types.integer.Integer"
    """<p>The minimum value to scale to in response to a scale-in activity.</p>"""
    max_capacity: "aws_sdk_ecs.types.integer.Integer"
    """<p>The maximum value to scale to in response to a scale-out activity.</p>"""
