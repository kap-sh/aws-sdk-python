"""Generated from Smithy shape ``com.amazonaws.ec2#EbsOptimizedInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.baseline_bandwidth_in_mbps
    import aws_sdk_ec2.types.baseline_iops
    import aws_sdk_ec2.types.baseline_throughput_in_m_bps
    import aws_sdk_ec2.types.maximum_bandwidth_in_mbps
    import aws_sdk_ec2.types.maximum_iops
    import aws_sdk_ec2.types.maximum_throughput_in_m_bps


class EbsOptimizedInfo(TypedDict):
    baseline_bandwidth_in_mbps: NotRequired[
        "aws_sdk_ec2.types.baseline_bandwidth_in_mbps.BaselineBandwidthInMbps"
    ]
    """<p>The baseline bandwidth performance for an EBS-optimized instance type, in Mbps.</p>"""
    baseline_throughput_in_m_bps: NotRequired[
        "aws_sdk_ec2.types.baseline_throughput_in_m_bps.BaselineThroughputInMBps"
    ]
    """<p>The baseline throughput performance for an EBS-optimized instance type, in MB/s.</p>"""
    baseline_iops: NotRequired["aws_sdk_ec2.types.baseline_iops.BaselineIops"]
    """<p>The baseline input/output storage operations per seconds for an EBS-optimized instance type.</p>"""
    maximum_bandwidth_in_mbps: NotRequired[
        "aws_sdk_ec2.types.maximum_bandwidth_in_mbps.MaximumBandwidthInMbps"
    ]
    """<p>The maximum bandwidth performance for an EBS-optimized instance type, in Mbps.</p>"""
    maximum_throughput_in_m_bps: NotRequired[
        "aws_sdk_ec2.types.maximum_throughput_in_m_bps.MaximumThroughputInMBps"
    ]
    """<p>The maximum throughput performance for an EBS-optimized instance type, in MB/s.</p>"""
    maximum_iops: NotRequired["aws_sdk_ec2.types.maximum_iops.MaximumIops"]
    """<p>The maximum input/output storage operations per second for an EBS-optimized instance type.</p>"""
