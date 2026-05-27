"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceNetworkPerformanceOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_bandwidth_weighting


class InstanceNetworkPerformanceOptions(TypedDict):
    bandwidth_weighting: NotRequired[
        "aws_sdk_ec2.types.instance_bandwidth_weighting.InstanceBandwidthWeighting"
    ]
    """<p>When you configure network bandwidth weighting, you can boost your baseline bandwidth for either networking or EBS by up to 25%. The total available baseline bandwidth for your instance remains the same. The default option uses the standard bandwidth configuration for your instance type.</p>"""
