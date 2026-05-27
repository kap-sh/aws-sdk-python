"""Generated from Smithy shape ``com.amazonaws.ecs#LoadBalancers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.load_balancer

LoadBalancers: TypeAlias = list["aws_sdk_ecs.types.load_balancer.LoadBalancer"]
