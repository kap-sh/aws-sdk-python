"""Generated from Smithy shape ``com.amazonaws.ec2#EbsOptimizedInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

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


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EbsOptimizedInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "baseline_bandwidth_in_mbps" in value:
        pairs.append(
            (
                f"{prefix}.BaselineBandwidthInMbps",
                str(value["baseline_bandwidth_in_mbps"]),
            )
        )
    if "baseline_throughput_in_m_bps" in value:
        pairs.append(
            (
                f"{prefix}.BaselineThroughputInMBps",
                str(value["baseline_throughput_in_m_bps"]),
            )
        )
    if "baseline_iops" in value:
        pairs.append((f"{prefix}.BaselineIops", str(value["baseline_iops"])))
    if "maximum_bandwidth_in_mbps" in value:
        pairs.append(
            (
                f"{prefix}.MaximumBandwidthInMbps",
                str(value["maximum_bandwidth_in_mbps"]),
            )
        )
    if "maximum_throughput_in_m_bps" in value:
        pairs.append(
            (
                f"{prefix}.MaximumThroughputInMBps",
                str(value["maximum_throughput_in_m_bps"]),
            )
        )
    if "maximum_iops" in value:
        pairs.append((f"{prefix}.MaximumIops", str(value["maximum_iops"])))


def deserialize_ec2_query(el: Element) -> EbsOptimizedInfo:
    out: EbsOptimizedInfo = {}  # type: ignore[typeddict-item]
    child_baseline_bandwidth_in_mbps = el.find("BaselineBandwidthInMbps")
    if child_baseline_bandwidth_in_mbps is not None:
        out["baseline_bandwidth_in_mbps"] = int(
            child_baseline_bandwidth_in_mbps.text or ""
        )
    child_baseline_throughput_in_m_bps = el.find("BaselineThroughputInMBps")
    if child_baseline_throughput_in_m_bps is not None:
        out["baseline_throughput_in_m_bps"] = float(
            child_baseline_throughput_in_m_bps.text or ""
        )
    child_baseline_iops = el.find("BaselineIops")
    if child_baseline_iops is not None:
        out["baseline_iops"] = int(child_baseline_iops.text or "")
    child_maximum_bandwidth_in_mbps = el.find("MaximumBandwidthInMbps")
    if child_maximum_bandwidth_in_mbps is not None:
        out["maximum_bandwidth_in_mbps"] = int(
            child_maximum_bandwidth_in_mbps.text or ""
        )
    child_maximum_throughput_in_m_bps = el.find("MaximumThroughputInMBps")
    if child_maximum_throughput_in_m_bps is not None:
        out["maximum_throughput_in_m_bps"] = float(
            child_maximum_throughput_in_m_bps.text or ""
        )
    child_maximum_iops = el.find("MaximumIops")
    if child_maximum_iops is not None:
        out["maximum_iops"] = int(child_maximum_iops.text or "")
    return out
