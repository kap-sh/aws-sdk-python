"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceRevisionLoadBalancers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service_revision_load_balancer

ServiceRevisionLoadBalancers: TypeAlias = list[
    "aws_sdk_ecs.types.service_revision_load_balancer.ServiceRevisionLoadBalancer"
]
