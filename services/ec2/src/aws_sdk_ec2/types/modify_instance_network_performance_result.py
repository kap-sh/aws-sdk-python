"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceNetworkPerformanceResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_bandwidth_weighting
    import aws_sdk_ec2.types.instance_id


class ModifyInstanceNetworkPerformanceResult(TypedDict):
    instance_id: NotRequired["aws_sdk_ec2.types.instance_id.InstanceId"]
    """<p>The instance ID that was updated.</p>"""
    bandwidth_weighting: NotRequired[
        "aws_sdk_ec2.types.instance_bandwidth_weighting.InstanceBandwidthWeighting"
    ]
    """<p>Contains the updated configuration for bandwidth weighting on the specified instance.</p>"""
