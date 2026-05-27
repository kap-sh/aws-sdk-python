"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstanceNetworkPerformanceRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.instance_bandwidth_weighting
    import aws_sdk_ec2.types.instance_id


class ModifyInstanceNetworkPerformanceRequest(TypedDict):
    instance_id: NotRequired["aws_sdk_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance to update.</p>"""
    bandwidth_weighting: NotRequired[
        "aws_sdk_ec2.types.instance_bandwidth_weighting.InstanceBandwidthWeighting"
    ]
    """<p>Specify the bandwidth weighting option to boost the associated type of baseline bandwidth, as follows:</p> <dl> <dt>default</dt> <dd> <p>This option uses the standard bandwidth configuration for your instance type.</p> </dd> <dt>vpc-1</dt> <dd> <p>This option boosts your networking baseline bandwidth and reduces your EBS baseline bandwidth.</p> </dd> <dt>ebs-1</dt> <dd> <p>This option boosts your EBS baseline bandwidth and reduces your networking baseline bandwidth.</p> </dd> </dl>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
