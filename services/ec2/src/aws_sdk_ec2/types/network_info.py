"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.bandwidth_weighting_type_list
    import aws_sdk_ec2.types.default_connection_tracking_configuration
    import aws_sdk_ec2.types.default_network_card_index
    import aws_sdk_ec2.types.efa_info
    import aws_sdk_ec2.types.efa_supported_flag
    import aws_sdk_ec2.types.ena_srd_supported
    import aws_sdk_ec2.types.ena_support
    import aws_sdk_ec2.types.encryption_in_transit_supported
    import aws_sdk_ec2.types.flexible_ena_queues_support
    import aws_sdk_ec2.types.ipv4_addresses_per_secondary_interface
    import aws_sdk_ec2.types.ipv6_flag
    import aws_sdk_ec2.types.max_ipv4_addr_per_interface
    import aws_sdk_ec2.types.max_ipv6_addr_per_interface
    import aws_sdk_ec2.types.max_network_interfaces
    import aws_sdk_ec2.types.maximum_network_cards
    import aws_sdk_ec2.types.maximum_secondary_network_interfaces
    import aws_sdk_ec2.types.network_card_info_list
    import aws_sdk_ec2.types.network_performance
    import aws_sdk_ec2.types.secondary_network_supported_flag


class NetworkInfo(TypedDict):
    network_performance: NotRequired[
        "aws_sdk_ec2.types.network_performance.NetworkPerformance"
    ]
    """<p>The network performance.</p>"""
    maximum_network_interfaces: NotRequired[
        "aws_sdk_ec2.types.max_network_interfaces.MaxNetworkInterfaces"
    ]
    """<p>The maximum number of network interfaces for the instance type.</p>"""
    maximum_network_cards: NotRequired[
        "aws_sdk_ec2.types.maximum_network_cards.MaximumNetworkCards"
    ]
    """<p>The maximum number of physical network cards that can be allocated to the instance.</p>"""
    default_network_card_index: NotRequired[
        "aws_sdk_ec2.types.default_network_card_index.DefaultNetworkCardIndex"
    ]
    """<p>The index of the default network card, starting at 0.</p>"""
    network_cards: NotRequired[
        "aws_sdk_ec2.types.network_card_info_list.NetworkCardInfoList"
    ]
    """<p>Describes the network cards for the instance type.</p>"""
    ipv4_addresses_per_interface: NotRequired[
        "aws_sdk_ec2.types.max_ipv4_addr_per_interface.MaxIpv4AddrPerInterface"
    ]
    """<p>The maximum number of IPv4 addresses per network interface.</p>"""
    ipv6_addresses_per_interface: NotRequired[
        "aws_sdk_ec2.types.max_ipv6_addr_per_interface.MaxIpv6AddrPerInterface"
    ]
    """<p>The maximum number of IPv6 addresses per network interface.</p>"""
    ipv6_supported: NotRequired["aws_sdk_ec2.types.ipv6_flag.Ipv6Flag"]
    """<p>Indicates whether IPv6 is supported.</p>"""
    ena_support: NotRequired["aws_sdk_ec2.types.ena_support.EnaSupport"]
    """<p>Indicates whether Elastic Network Adapter (ENA) is supported.</p>"""
    efa_supported: NotRequired["aws_sdk_ec2.types.efa_supported_flag.EfaSupportedFlag"]
    """<p>Indicates whether Elastic Fabric Adapter (EFA) is supported.</p>"""
    efa_info: NotRequired["aws_sdk_ec2.types.efa_info.EfaInfo"]
    """<p>Describes the Elastic Fabric Adapters for the instance type.</p>"""
    encryption_in_transit_supported: NotRequired[
        "aws_sdk_ec2.types.encryption_in_transit_supported.EncryptionInTransitSupported"
    ]
    """<p>Indicates whether the instance type automatically encrypts in-transit traffic between instances.</p>"""
    ena_srd_supported: NotRequired[
        "aws_sdk_ec2.types.ena_srd_supported.EnaSrdSupported"
    ]
    """<p>Indicates whether the instance type supports ENA Express. ENA Express uses Amazon Web Services Scalable Reliable Datagram (SRD) technology to increase the maximum bandwidth used per stream and minimize tail latency of network traffic between EC2 instances.</p>"""
    bandwidth_weightings: NotRequired[
        "aws_sdk_ec2.types.bandwidth_weighting_type_list.BandwidthWeightingTypeList"
    ]
    """<p>A list of valid settings for configurable bandwidth weighting for the instance type, if supported.</p>"""
    flexible_ena_queues_support: NotRequired[
        "aws_sdk_ec2.types.flexible_ena_queues_support.FlexibleEnaQueuesSupport"
    ]
    """<p>Indicates whether changing the number of ENA queues is supported.</p>"""
    connection_tracking_configuration: NotRequired[
        "aws_sdk_ec2.types.default_connection_tracking_configuration.DefaultConnectionTrackingConfiguration"
    ]
    """<p>Indicates conntrack information for the instance type</p>"""
    secondary_network_supported: NotRequired[
        "aws_sdk_ec2.types.secondary_network_supported_flag.SecondaryNetworkSupportedFlag"
    ]
    """<p>Indicates whether secondary interface attachments from secondary network are supported.</p>"""
    maximum_secondary_network_interfaces: NotRequired[
        "aws_sdk_ec2.types.maximum_secondary_network_interfaces.MaximumSecondaryNetworkInterfaces"
    ]
    """<p>The maximum number of secondary interfaces for the instance type.</p>"""
    ipv4_addresses_per_secondary_interface: NotRequired[
        "aws_sdk_ec2.types.ipv4_addresses_per_secondary_interface.Ipv4AddressesPerSecondaryInterface"
    ]
    """<p>The maximum number of IPv4 addresses per secondary interface.</p>"""
