"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkCardInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

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
