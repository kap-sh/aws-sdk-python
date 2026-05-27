"""Generated from Smithy shape ``com.amazonaws.ec2#AnalysisLoadBalancerTarget``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.analysis_component
    import aws_sdk_ec2.types.ip_address
    import aws_sdk_ec2.types.port
    import aws_sdk_ec2.types.string


class AnalysisLoadBalancerTarget(TypedDict):
    address: NotRequired["aws_sdk_ec2.types.ip_address.IpAddress"]
    """<p>The IP address.</p>"""
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone.</p>"""
    availability_zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Availability Zone.</p>"""
    instance: NotRequired["aws_sdk_ec2.types.analysis_component.AnalysisComponent"]
    """<p>Information about the instance.</p>"""
    port: NotRequired["aws_sdk_ec2.types.port.Port"]
    """<p>The port on which the target is listening.</p>"""
