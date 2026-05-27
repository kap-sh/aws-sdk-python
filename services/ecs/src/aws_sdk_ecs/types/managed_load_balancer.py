"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedLoadBalancer``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.managed_resource_status
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_list
    import aws_sdk_ecs.types.timestamp


class ManagedLoadBalancer(TypedDict):
    arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the load balancer.</p>"""
    status: "aws_sdk_ecs.types.managed_resource_status.ManagedResourceStatus"
    """<p>The status of the load balancer.</p>"""
    status_reason: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>Information about why the load balancer is in the current status.</p>"""
    updated_at: "aws_sdk_ecs.types.timestamp.Timestamp"
    """<p>The Unix timestamp for when this load balancer was most recently updated.</p>"""
    scheme: "aws_sdk_ecs.types.string.String"
    """<p>The scheme of the load balancer. By default, the scheme of the load balancer is <code>internet-facing</code>.</p>"""
    subnet_ids: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>The IDs of the subnets associated with the load balancer.</p>"""
    security_group_ids: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>The IDs of the security groups associated with the load balancer.</p>"""
