"""Generated from Smithy shape ``com.amazonaws.ec2#ClassicLoadBalancers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.classic_load_balancer

ClassicLoadBalancers: TypeAlias = list[
    "aws_sdk_ec2.types.classic_load_balancer.ClassicLoadBalancer"
]
