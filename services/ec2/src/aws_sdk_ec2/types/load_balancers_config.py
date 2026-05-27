"""Generated from Smithy shape ``com.amazonaws.ec2#LoadBalancersConfig``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.classic_load_balancers_config
    import aws_sdk_ec2.types.target_groups_config


class LoadBalancersConfig(TypedDict):
    classic_load_balancers_config: NotRequired[
        "aws_sdk_ec2.types.classic_load_balancers_config.ClassicLoadBalancersConfig"
    ]
    """<p>The Classic Load Balancers.</p>"""
    target_groups_config: NotRequired[
        "aws_sdk_ec2.types.target_groups_config.TargetGroupsConfig"
    ]
    """<p>The target groups.</p>"""
