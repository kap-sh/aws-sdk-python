"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkCardInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.additional_flexible_network_interfaces
    import capo_ec2.types.baseline_bandwidth_in_gbps
    import capo_ec2.types.default_ena_queue_count_per_interface
    import capo_ec2.types.max_network_interfaces
    import capo_ec2.types.maximum_ena_queue_count
    import capo_ec2.types.maximum_ena_queue_count_per_interface
    import capo_ec2.types.network_card_index
    import capo_ec2.types.network_performance
    import capo_ec2.types.peak_bandwidth_in_gbps


class NetworkCardInfo(TypedDict, closed=True):
    network_card_index: NotRequired[
        "capo_ec2.types.network_card_index.NetworkCardIndex"
    ]
    """<p>The index of the network card.</p>"""
    network_performance: NotRequired[
        "capo_ec2.types.network_performance.NetworkPerformance"
    ]
    """<p>The network performance of the network card.</p>"""
    maximum_network_interfaces: NotRequired[
        "capo_ec2.types.max_network_interfaces.MaxNetworkInterfaces"
    ]
    """<p>The maximum number of network interfaces for the network card.</p>"""
    additional_flexible_network_interfaces: NotRequired[
        "capo_ec2.types.additional_flexible_network_interfaces.AdditionalFlexibleNetworkInterfaces"
    ]
    """<p>The number of additional network interfaces that can be attached to an instance when using flexible Elastic Network Adapter (ENA) queues. This number is in addition to the base number specified by <code>maximumNetworkInterfaces</code>.</p>"""
    baseline_bandwidth_in_gbps: NotRequired[
        "capo_ec2.types.baseline_bandwidth_in_gbps.BaselineBandwidthInGbps"
    ]
    """<p>The baseline network performance of the network card, in Gbps.</p>"""
    peak_bandwidth_in_gbps: NotRequired[
        "capo_ec2.types.peak_bandwidth_in_gbps.PeakBandwidthInGbps"
    ]
    """<p>The peak (burst) network performance of the network card, in Gbps.</p>"""
    default_ena_queue_count_per_interface: NotRequired[
        "capo_ec2.types.default_ena_queue_count_per_interface.DefaultEnaQueueCountPerInterface"
    ]
    """<p>The default number of the ENA queues for each interface.</p>"""
    maximum_ena_queue_count: NotRequired[
        "capo_ec2.types.maximum_ena_queue_count.MaximumEnaQueueCount"
    ]
    """<p>The maximum number of the ENA queues.</p>"""
    maximum_ena_queue_count_per_interface: NotRequired[
        "capo_ec2.types.maximum_ena_queue_count_per_interface.MaximumEnaQueueCountPerInterface"
    ]
    """<p>The maximum number of the ENA queues for each interface.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NetworkCardInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "network_card_index" in value:
        pairs.append(
            (f"{key_prefix}NetworkCardIndex", str(value["network_card_index"]))
        )
    if "network_performance" in value:
        pairs.append(
            (f"{key_prefix}NetworkPerformance", str(value["network_performance"]))
        )
    if "maximum_network_interfaces" in value:
        pairs.append(
            (
                f"{key_prefix}MaximumNetworkInterfaces",
                str(value["maximum_network_interfaces"]),
            )
        )
    if "additional_flexible_network_interfaces" in value:
        pairs.append(
            (
                f"{key_prefix}AdditionalFlexibleNetworkInterfaces",
                str(value["additional_flexible_network_interfaces"]),
            )
        )
    if "baseline_bandwidth_in_gbps" in value:
        pairs.append(
            (
                f"{key_prefix}BaselineBandwidthInGbps",
                str(value["baseline_bandwidth_in_gbps"]),
            )
        )
    if "peak_bandwidth_in_gbps" in value:
        pairs.append(
            (f"{key_prefix}PeakBandwidthInGbps", str(value["peak_bandwidth_in_gbps"]))
        )
    if "default_ena_queue_count_per_interface" in value:
        pairs.append(
            (
                f"{key_prefix}DefaultEnaQueueCountPerInterface",
                str(value["default_ena_queue_count_per_interface"]),
            )
        )
    if "maximum_ena_queue_count" in value:
        pairs.append(
            (f"{key_prefix}MaximumEnaQueueCount", str(value["maximum_ena_queue_count"]))
        )
    if "maximum_ena_queue_count_per_interface" in value:
        pairs.append(
            (
                f"{key_prefix}MaximumEnaQueueCountPerInterface",
                str(value["maximum_ena_queue_count_per_interface"]),
            )
        )


def deserialize_ec2_query(el: Element) -> NetworkCardInfo:
    out: NetworkCardInfo = {}  # type: ignore[typeddict-item]
    child_network_card_index = el.find("networkCardIndex")
    if child_network_card_index is not None:
        out["network_card_index"] = int(child_network_card_index.text or "")
    child_network_performance = el.find("networkPerformance")
    if child_network_performance is not None:
        out["network_performance"] = str(child_network_performance.text or "")
    child_maximum_network_interfaces = el.find("maximumNetworkInterfaces")
    if child_maximum_network_interfaces is not None:
        out["maximum_network_interfaces"] = int(
            child_maximum_network_interfaces.text or ""
        )
    child_additional_flexible_network_interfaces = el.find(
        "additionalFlexibleNetworkInterfaces"
    )
    if child_additional_flexible_network_interfaces is not None:
        out["additional_flexible_network_interfaces"] = int(
            child_additional_flexible_network_interfaces.text or ""
        )
    child_baseline_bandwidth_in_gbps = el.find("baselineBandwidthInGbps")
    if child_baseline_bandwidth_in_gbps is not None:
        out["baseline_bandwidth_in_gbps"] = float(
            child_baseline_bandwidth_in_gbps.text or ""
        )
    child_peak_bandwidth_in_gbps = el.find("peakBandwidthInGbps")
    if child_peak_bandwidth_in_gbps is not None:
        out["peak_bandwidth_in_gbps"] = float(child_peak_bandwidth_in_gbps.text or "")
    child_default_ena_queue_count_per_interface = el.find(
        "defaultEnaQueueCountPerInterface"
    )
    if child_default_ena_queue_count_per_interface is not None:
        out["default_ena_queue_count_per_interface"] = int(
            child_default_ena_queue_count_per_interface.text or ""
        )
    child_maximum_ena_queue_count = el.find("maximumEnaQueueCount")
    if child_maximum_ena_queue_count is not None:
        out["maximum_ena_queue_count"] = int(child_maximum_ena_queue_count.text or "")
    child_maximum_ena_queue_count_per_interface = el.find(
        "maximumEnaQueueCountPerInterface"
    )
    if child_maximum_ena_queue_count_per_interface is not None:
        out["maximum_ena_queue_count_per_interface"] = int(
            child_maximum_ena_queue_count_per_interface.text or ""
        )
    return out
