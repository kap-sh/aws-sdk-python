"""Generated from Smithy shape ``com.amazonaws.ec2#EbsCardInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.baseline_bandwidth_in_mbps
    import aws_sdk_ec2.types.baseline_iops
    import aws_sdk_ec2.types.baseline_throughput_in_m_bps
    import aws_sdk_ec2.types.ebs_card_index
    import aws_sdk_ec2.types.maximum_bandwidth_in_mbps
    import aws_sdk_ec2.types.maximum_iops
    import aws_sdk_ec2.types.maximum_throughput_in_m_bps


class EbsCardInfo(TypedDict):
    ebs_card_index: NotRequired["aws_sdk_ec2.types.ebs_card_index.EbsCardIndex"]
    """<p>The index of the EBS card.</p>"""
    baseline_bandwidth_in_mbps: NotRequired[
        "aws_sdk_ec2.types.baseline_bandwidth_in_mbps.BaselineBandwidthInMbps"
    ]
    """<p>The baseline bandwidth performance for the EBS card, in Mbps.</p>"""
    baseline_throughput_in_m_bps: NotRequired[
        "aws_sdk_ec2.types.baseline_throughput_in_m_bps.BaselineThroughputInMBps"
    ]
    """<p>The baseline throughput performance for the EBS card, in MBps.</p>"""
    baseline_iops: NotRequired["aws_sdk_ec2.types.baseline_iops.BaselineIops"]
    """<p>The baseline IOPS performance for the EBS card.</p>"""
    maximum_bandwidth_in_mbps: NotRequired[
        "aws_sdk_ec2.types.maximum_bandwidth_in_mbps.MaximumBandwidthInMbps"
    ]
    """<p>The maximum bandwidth performance for the EBS card, in Mbps.</p>"""
    maximum_throughput_in_m_bps: NotRequired[
        "aws_sdk_ec2.types.maximum_throughput_in_m_bps.MaximumThroughputInMBps"
    ]
    """<p>The maximum throughput performance for the EBS card, in MBps.</p>"""
    maximum_iops: NotRequired["aws_sdk_ec2.types.maximum_iops.MaximumIops"]
    """<p>The maximum IOPS performance for the EBS card.</p>"""
