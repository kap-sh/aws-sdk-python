"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

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


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NetworkInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
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
    if "maximum_network_cards" in value:
        pairs.append(
            (f"{prefix}.MaximumNetworkCards", str(value["maximum_network_cards"]))
        )
    if "default_network_card_index" in value:
        pairs.append(
            (
                f"{prefix}.DefaultNetworkCardIndex",
                str(value["default_network_card_index"]),
            )
        )
    if "network_cards" in value:
        import aws_sdk_ec2.types.network_card_info_list

        aws_sdk_ec2.types.network_card_info_list.serialize_ec2_query(
            value["network_cards"], pairs, f"{prefix}.NetworkCards"
        )
    if "ipv4_addresses_per_interface" in value:
        pairs.append(
            (
                f"{prefix}.Ipv4AddressesPerInterface",
                str(value["ipv4_addresses_per_interface"]),
            )
        )
    if "ipv6_addresses_per_interface" in value:
        pairs.append(
            (
                f"{prefix}.Ipv6AddressesPerInterface",
                str(value["ipv6_addresses_per_interface"]),
            )
        )
    if "ipv6_supported" in value:
        pairs.append(
            (f"{prefix}.Ipv6Supported", "true" if value["ipv6_supported"] else "false")
        )
    if "ena_support" in value:
        import aws_sdk_ec2.types.ena_support

        aws_sdk_ec2.types.ena_support.serialize_ec2_query(
            value["ena_support"], pairs, f"{prefix}.EnaSupport"
        )
    if "efa_supported" in value:
        pairs.append(
            (f"{prefix}.EfaSupported", "true" if value["efa_supported"] else "false")
        )
    if "efa_info" in value:
        import aws_sdk_ec2.types.efa_info

        aws_sdk_ec2.types.efa_info.serialize_ec2_query(
            value["efa_info"], pairs, f"{prefix}.EfaInfo"
        )
    if "encryption_in_transit_supported" in value:
        pairs.append(
            (
                f"{prefix}.EncryptionInTransitSupported",
                "true" if value["encryption_in_transit_supported"] else "false",
            )
        )
    if "ena_srd_supported" in value:
        pairs.append(
            (
                f"{prefix}.EnaSrdSupported",
                "true" if value["ena_srd_supported"] else "false",
            )
        )
    if "bandwidth_weightings" in value:
        import aws_sdk_ec2.types.bandwidth_weighting_type_list

        aws_sdk_ec2.types.bandwidth_weighting_type_list.serialize_ec2_query(
            value["bandwidth_weightings"], pairs, f"{prefix}.BandwidthWeightings"
        )
    if "flexible_ena_queues_support" in value:
        import aws_sdk_ec2.types.flexible_ena_queues_support

        aws_sdk_ec2.types.flexible_ena_queues_support.serialize_ec2_query(
            value["flexible_ena_queues_support"],
            pairs,
            f"{prefix}.FlexibleEnaQueuesSupport",
        )
    if "connection_tracking_configuration" in value:
        import aws_sdk_ec2.types.default_connection_tracking_configuration

        aws_sdk_ec2.types.default_connection_tracking_configuration.serialize_ec2_query(
            value["connection_tracking_configuration"],
            pairs,
            f"{prefix}.ConnectionTrackingConfiguration",
        )
    if "secondary_network_supported" in value:
        pairs.append(
            (
                f"{prefix}.SecondaryNetworkSupported",
                "true" if value["secondary_network_supported"] else "false",
            )
        )
    if "maximum_secondary_network_interfaces" in value:
        pairs.append(
            (
                f"{prefix}.MaximumSecondaryNetworkInterfaces",
                str(value["maximum_secondary_network_interfaces"]),
            )
        )
    if "ipv4_addresses_per_secondary_interface" in value:
        pairs.append(
            (
                f"{prefix}.Ipv4AddressesPerSecondaryInterface",
                str(value["ipv4_addresses_per_secondary_interface"]),
            )
        )


def deserialize_ec2_query(el: Element) -> NetworkInfo:
    out: NetworkInfo = {}  # type: ignore[typeddict-item]
    child_network_performance = el.find("NetworkPerformance")
    if child_network_performance is not None:
        out["network_performance"] = str(child_network_performance.text or "")
    child_maximum_network_interfaces = el.find("MaximumNetworkInterfaces")
    if child_maximum_network_interfaces is not None:
        out["maximum_network_interfaces"] = int(
            child_maximum_network_interfaces.text or ""
        )
    child_maximum_network_cards = el.find("MaximumNetworkCards")
    if child_maximum_network_cards is not None:
        out["maximum_network_cards"] = int(child_maximum_network_cards.text or "")
    child_default_network_card_index = el.find("DefaultNetworkCardIndex")
    if child_default_network_card_index is not None:
        out["default_network_card_index"] = int(
            child_default_network_card_index.text or ""
        )
    if el.find("NetworkCards") is not None:
        import aws_sdk_ec2.types.network_card_info_list

        out["network_cards"] = (
            aws_sdk_ec2.types.network_card_info_list.deserialize_ec2_query(
                el, "NetworkCards"
            )
        )
    child_ipv4_addresses_per_interface = el.find("Ipv4AddressesPerInterface")
    if child_ipv4_addresses_per_interface is not None:
        out["ipv4_addresses_per_interface"] = int(
            child_ipv4_addresses_per_interface.text or ""
        )
    child_ipv6_addresses_per_interface = el.find("Ipv6AddressesPerInterface")
    if child_ipv6_addresses_per_interface is not None:
        out["ipv6_addresses_per_interface"] = int(
            child_ipv6_addresses_per_interface.text or ""
        )
    child_ipv6_supported = el.find("Ipv6Supported")
    if child_ipv6_supported is not None:
        out["ipv6_supported"] = (child_ipv6_supported.text or "").lower() == "true"
    child_ena_support = el.find("EnaSupport")
    if child_ena_support is not None:
        import aws_sdk_ec2.types.ena_support

        out["ena_support"] = aws_sdk_ec2.types.ena_support.deserialize_ec2_query(
            child_ena_support
        )
    child_efa_supported = el.find("EfaSupported")
    if child_efa_supported is not None:
        out["efa_supported"] = (child_efa_supported.text or "").lower() == "true"
    child_efa_info = el.find("EfaInfo")
    if child_efa_info is not None:
        import aws_sdk_ec2.types.efa_info

        out["efa_info"] = aws_sdk_ec2.types.efa_info.deserialize_ec2_query(
            child_efa_info
        )
    child_encryption_in_transit_supported = el.find("EncryptionInTransitSupported")
    if child_encryption_in_transit_supported is not None:
        out["encryption_in_transit_supported"] = (
            child_encryption_in_transit_supported.text or ""
        ).lower() == "true"
    child_ena_srd_supported = el.find("EnaSrdSupported")
    if child_ena_srd_supported is not None:
        out["ena_srd_supported"] = (
            child_ena_srd_supported.text or ""
        ).lower() == "true"
    if el.find("BandwidthWeightings") is not None:
        import aws_sdk_ec2.types.bandwidth_weighting_type_list

        out["bandwidth_weightings"] = (
            aws_sdk_ec2.types.bandwidth_weighting_type_list.deserialize_ec2_query(
                el, "BandwidthWeightings"
            )
        )
    child_flexible_ena_queues_support = el.find("FlexibleEnaQueuesSupport")
    if child_flexible_ena_queues_support is not None:
        import aws_sdk_ec2.types.flexible_ena_queues_support

        out["flexible_ena_queues_support"] = (
            aws_sdk_ec2.types.flexible_ena_queues_support.deserialize_ec2_query(
                child_flexible_ena_queues_support
            )
        )
    child_connection_tracking_configuration = el.find("ConnectionTrackingConfiguration")
    if child_connection_tracking_configuration is not None:
        import aws_sdk_ec2.types.default_connection_tracking_configuration

        out["connection_tracking_configuration"] = (
            aws_sdk_ec2.types.default_connection_tracking_configuration.deserialize_ec2_query(
                child_connection_tracking_configuration
            )
        )
    child_secondary_network_supported = el.find("SecondaryNetworkSupported")
    if child_secondary_network_supported is not None:
        out["secondary_network_supported"] = (
            child_secondary_network_supported.text or ""
        ).lower() == "true"
    child_maximum_secondary_network_interfaces = el.find(
        "MaximumSecondaryNetworkInterfaces"
    )
    if child_maximum_secondary_network_interfaces is not None:
        out["maximum_secondary_network_interfaces"] = int(
            child_maximum_secondary_network_interfaces.text or ""
        )
    child_ipv4_addresses_per_secondary_interface = el.find(
        "Ipv4AddressesPerSecondaryInterface"
    )
    if child_ipv4_addresses_per_secondary_interface is not None:
        out["ipv4_addresses_per_secondary_interface"] = int(
            child_ipv4_addresses_per_secondary_interface.text or ""
        )
    return out
