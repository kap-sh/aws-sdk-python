"""Generated from Smithy shape ``com.amazonaws.ec2#AnalysisLoadBalancerListener``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.port


class AnalysisLoadBalancerListener(TypedDict):
    load_balancer_port: NotRequired["aws_sdk_ec2.types.port.Port"]
    """<p>The port on which the load balancer is listening.</p>"""
    instance_port: NotRequired["aws_sdk_ec2.types.port.Port"]
    """<p>[Classic Load Balancers] The back-end port for the listener.</p>"""
