"""Generated from Smithy shape ``com.amazonaws.ec2#ClassicLoadBalancersConfig``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.classic_load_balancers


class ClassicLoadBalancersConfig(TypedDict):
    classic_load_balancers: NotRequired[
        "aws_sdk_ec2.types.classic_load_balancers.ClassicLoadBalancers"
    ]
    """<p>One or more Classic Load Balancers.</p>"""
