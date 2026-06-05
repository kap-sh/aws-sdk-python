"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkCardInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.additional_flexible_network_interfaces
    import aws_sdk_ec2.types.baseline_bandwidth_in_gbps
    import aws_sdk_ec2.types.default_ena_queue_count_per_interface
    import aws_sdk_ec2.types.max_network_interfaces
    import aws_sdk_ec2.types.maximum_ena_queue_count
    import aws_sdk_ec2.types.maximum_ena_queue_count_per_interface
    import aws_sdk_ec2.types.network_card_index
    import aws_sdk_ec2.types.network_performance
    import aws_sdk_ec2.types.peak_bandwidth_in_gbps


class NetworkCardInfo(TypedDict):
    network_card_index: NotRequired[
        "aws_sdk_ec2.types.network_card_index.NetworkCardIndex"
    ]
    """<p>The index of the network card.</p>"""
    network_performance: NotRequired[
        "aws_sdk_ec2.types.network_performance.NetworkPerformance"
    ]
    """<p>The network performance of the network card.</p>"""
    maximum_network_interfaces: NotRequired[
        "aws_sdk_ec2.types.max_network_interfaces.MaxNetworkInterfaces"
    ]
    """<p>The maximum number of network interfaces for the network card.</p>"""
    additional_flexible_network_interfaces: NotRequired[
        "aws_sdk_ec2.types.additional_flexible_network_interfaces.AdditionalFlexibleNetworkInterfaces"
    ]
    """<p>The number of additional network interfaces that can be attached to an instance when using flexible Elastic Network Adapter (ENA) queues. This number is in addition to the base number specified by <code>maximumNetworkInterfaces</code>.</p>"""
    baseline_bandwidth_in_gbps: NotRequired[
        "aws_sdk_ec2.types.baseline_bandwidth_in_gbps.BaselineBandwidthInGbps"
    ]
    """<p>The baseline network performance of the network card, in Gbps.</p>"""
    peak_bandwidth_in_gbps: NotRequired[
        "aws_sdk_ec2.types.peak_bandwidth_in_gbps.PeakBandwidthInGbps"
    ]
    """<p>The peak (burst) network performance of the network card, in Gbps.</p>"""
    default_ena_queue_count_per_interface: NotRequired[
        "aws_sdk_ec2.types.default_ena_queue_count_per_interface.DefaultEnaQueueCountPerInterface"
    ]
    """<p>The default number of the ENA queues for each interface.</p>"""
    maximum_ena_queue_count: NotRequired[
        "aws_sdk_ec2.types.maximum_ena_queue_count.MaximumEnaQueueCount"
    ]
    """<p>The maximum number of the ENA queues.</p>"""
    maximum_ena_queue_count_per_interface: NotRequired[
        "aws_sdk_ec2.types.maximum_ena_queue_count_per_interface.MaximumEnaQueueCountPerInterface"
    ]
    """<p>The maximum number of the ENA queues for each interface.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NetworkCardInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "network_card_index" in value:
        pairs.append((f"{prefix}.NetworkCardIndex", str(value["network_card_index"])))
    if "network_performance" in value:
        pairs.append(
            (f"{prefix}.NetworkPerformance", str(value["network_performance"]))
        )
    if "maximum_network_interfaces" in value:
        pairs.append(
            (
                f"{prefix}.MaximumNetworkInterfaces",
                str(value["maximum_network_interfaces"]),
            )
        )
    if "additional_flexible_network_interfaces" in value:
        pairs.append(
            (
                f"{prefix}.AdditionalFlexibleNetworkInterfaces",
                str(value["additional_flexible_network_interfaces"]),
            )
        )
    if "baseline_bandwidth_in_gbps" in value:
        pairs.append(
            (
                f"{prefix}.BaselineBandwidthInGbps",
                str(value["baseline_bandwidth_in_gbps"]),
            )
        )
    if "peak_bandwidth_in_gbps" in value:
        pairs.append(
            (f"{prefix}.PeakBandwidthInGbps", str(value["peak_bandwidth_in_gbps"]))
        )
    if "default_ena_queue_count_per_interface" in value:
        pairs.append(
            (
                f"{prefix}.DefaultEnaQueueCountPerInterface",
                str(value["default_ena_queue_count_per_interface"]),
            )
        )
    if "maximum_ena_queue_count" in value:
        pairs.append(
            (f"{prefix}.MaximumEnaQueueCount", str(value["maximum_ena_queue_count"]))
        )
    if "maximum_ena_queue_count_per_interface" in value:
        pairs.append(
            (
                f"{prefix}.MaximumEnaQueueCountPerInterface",
                str(value["maximum_ena_queue_count_per_interface"]),
            )
        )


def deserialize_ec2_query(el: Element) -> NetworkCardInfo:
    out: NetworkCardInfo = {}  # type: ignore[typeddict-item]
    child_network_card_index = el.find("NetworkCardIndex")
    if child_network_card_index is not None:
        out["network_card_index"] = int(child_network_card_index.text or "")
    child_network_performance = el.find("NetworkPerformance")
    if child_network_performance is not None:
        out["network_performance"] = str(child_network_performance.text or "")
    child_maximum_network_interfaces = el.find("MaximumNetworkInterfaces")
    if child_maximum_network_interfaces is not None:
        out["maximum_network_interfaces"] = int(
            child_maximum_network_interfaces.text or ""
        )
    child_additional_flexible_network_interfaces = el.find(
        "AdditionalFlexibleNetworkInterfaces"
    )
    if child_additional_flexible_network_interfaces is not None:
        out["additional_flexible_network_interfaces"] = int(
            child_additional_flexible_network_interfaces.text or ""
        )
    child_baseline_bandwidth_in_gbps = el.find("BaselineBandwidthInGbps")
    if child_baseline_bandwidth_in_gbps is not None:
        out["baseline_bandwidth_in_gbps"] = float(
            child_baseline_bandwidth_in_gbps.text or ""
        )
    child_peak_bandwidth_in_gbps = el.find("PeakBandwidthInGbps")
    if child_peak_bandwidth_in_gbps is not None:
        out["peak_bandwidth_in_gbps"] = float(child_peak_bandwidth_in_gbps.text or "")
    child_default_ena_queue_count_per_interface = el.find(
        "DefaultEnaQueueCountPerInterface"
    )
    if child_default_ena_queue_count_per_interface is not None:
        out["default_ena_queue_count_per_interface"] = int(
            child_default_ena_queue_count_per_interface.text or ""
        )
    child_maximum_ena_queue_count = el.find("MaximumEnaQueueCount")
    if child_maximum_ena_queue_count is not None:
        out["maximum_ena_queue_count"] = int(child_maximum_ena_queue_count.text or "")
    child_maximum_ena_queue_count_per_interface = el.find(
        "MaximumEnaQueueCountPerInterface"
    )
    if child_maximum_ena_queue_count_per_interface is not None:
        out["maximum_ena_queue_count_per_interface"] = int(
            child_maximum_ena_queue_count_per_interface.text or ""
        )
    return out
