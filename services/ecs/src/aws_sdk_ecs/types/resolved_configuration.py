"""Generated from Smithy shape ``com.amazonaws.ecs#ResolvedConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service_revision_load_balancers


class ResolvedConfiguration(TypedDict):
    load_balancers: NotRequired[
        "aws_sdk_ecs.types.service_revision_load_balancers.ServiceRevisionLoadBalancers"
    ]
    """<p>The resolved load balancer configuration for the service revision. This includes information about which target groups serve traffic and which listener rules direct traffic to them.</p>"""
