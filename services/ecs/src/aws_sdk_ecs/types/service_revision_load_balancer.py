"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceRevisionLoadBalancer``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class ServiceRevisionLoadBalancer(TypedDict):
    target_group_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the target group associated with the service revision.</p>"""
    production_listener_rule: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the production listener rule or listener that directs traffic to the target group associated with the service revision.</p>"""
