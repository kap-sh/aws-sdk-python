"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.bandwidth_weighting_type_list
    import capo_ec2.types.default_connection_tracking_configuration
    import capo_ec2.types.default_network_card_index
    import capo_ec2.types.efa_info
    import capo_ec2.types.efa_supported_flag
    import capo_ec2.types.ena_srd_supported
    import capo_ec2.types.ena_support
    import capo_ec2.types.encryption_in_transit_supported
    import capo_ec2.types.flexible_ena_queues_support
    import capo_ec2.types.ipv4_addresses_per_secondary_interface
    import capo_ec2.types.ipv6_flag
    import capo_ec2.types.max_ipv4_addr_per_interface
    import capo_ec2.types.max_ipv6_addr_per_interface
    import capo_ec2.types.max_network_interfaces
    import capo_ec2.types.maximum_network_cards
    import capo_ec2.types.maximum_secondary_network_interfaces
    import capo_ec2.types.network_card_info_list
    import capo_ec2.types.network_performance
    import capo_ec2.types.secondary_network_supported_flag


class NetworkInfo(TypedDict, closed=True):
    network_performance: NotRequired[
        "capo_ec2.types.network_performance.NetworkPerformance"
    ]
    """<p>The network performance.</p>"""
    maximum_network_interfaces: NotRequired[
        "capo_ec2.types.max_network_interfaces.MaxNetworkInterfaces"
    ]
    """<p>The maximum number of network interfaces for the instance type.</p>"""
    maximum_network_cards: NotRequired[
        "capo_ec2.types.maximum_network_cards.MaximumNetworkCards"
    ]
    """<p>The maximum number of physical network cards that can be allocated to the instance.</p>"""
    default_network_card_index: NotRequired[
        "capo_ec2.types.default_network_card_index.DefaultNetworkCardIndex"
    ]
    """<p>The index of the default network card, starting at 0.</p>"""
    network_cards: NotRequired[
        "capo_ec2.types.network_card_info_list.NetworkCardInfoList"
    ]
    """<p>Describes the network cards for the instance type.</p>"""
    ipv4_addresses_per_interface: NotRequired[
        "capo_ec2.types.max_ipv4_addr_per_interface.MaxIpv4AddrPerInterface"
    ]
    """<p>The maximum number of IPv4 addresses per network interface.</p>"""
    ipv6_addresses_per_interface: NotRequired[
        "capo_ec2.types.max_ipv6_addr_per_interface.MaxIpv6AddrPerInterface"
    ]
    """<p>The maximum number of IPv6 addresses per network interface.</p>"""
    ipv6_supported: NotRequired["capo_ec2.types.ipv6_flag.Ipv6Flag"]
    """<p>Indicates whether IPv6 is supported.</p>"""
    ena_support: NotRequired["capo_ec2.types.ena_support.EnaSupport"]
    """<p>Indicates whether Elastic Network Adapter (ENA) is supported.</p>"""
    efa_supported: NotRequired["capo_ec2.types.efa_supported_flag.EfaSupportedFlag"]
    """<p>Indicates whether Elastic Fabric Adapter (EFA) is supported.</p>"""
    efa_info: NotRequired["capo_ec2.types.efa_info.EfaInfo"]
    """<p>Describes the Elastic Fabric Adapters for the instance type.</p>"""
    encryption_in_transit_supported: NotRequired[
        "capo_ec2.types.encryption_in_transit_supported.EncryptionInTransitSupported"
    ]
    """<p>Indicates whether the instance type automatically encrypts in-transit traffic between instances.</p>"""
    ena_srd_supported: NotRequired["capo_ec2.types.ena_srd_supported.EnaSrdSupported"]
    """<p>Indicates whether the instance type supports ENA Express. ENA Express uses Amazon Web Services Scalable Reliable Datagram (SRD) technology to increase the maximum bandwidth used per stream and minimize tail latency of network traffic between EC2 instances.</p>"""
    bandwidth_weightings: NotRequired[
        "capo_ec2.types.bandwidth_weighting_type_list.BandwidthWeightingTypeList"
    ]
    """<p>A list of valid settings for configurable bandwidth weighting for the instance type, if supported.</p>"""
    flexible_ena_queues_support: NotRequired[
        "capo_ec2.types.flexible_ena_queues_support.FlexibleEnaQueuesSupport"
    ]
    """<p>Indicates whether changing the number of ENA queues is supported.</p>"""
    connection_tracking_configuration: NotRequired[
        "capo_ec2.types.default_connection_tracking_configuration.DefaultConnectionTrackingConfiguration"
    ]
    """<p>Indicates conntrack information for the instance type</p>"""
    secondary_network_supported: NotRequired[
        "capo_ec2.types.secondary_network_supported_flag.SecondaryNetworkSupportedFlag"
    ]
    """<p>Indicates whether secondary interface attachments from secondary network are supported.</p>"""
    maximum_secondary_network_interfaces: NotRequired[
        "capo_ec2.types.maximum_secondary_network_interfaces.MaximumSecondaryNetworkInterfaces"
    ]
    """<p>The maximum number of secondary interfaces for the instance type.</p>"""
    ipv4_addresses_per_secondary_interface: NotRequired[
        "capo_ec2.types.ipv4_addresses_per_secondary_interface.Ipv4AddressesPerSecondaryInterface"
    ]
    """<p>The maximum number of IPv4 addresses per secondary interface.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NetworkInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
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
    if "maximum_network_cards" in value:
        pairs.append(
            (f"{key_prefix}MaximumNetworkCards", str(value["maximum_network_cards"]))
        )
    if "default_network_card_index" in value:
        pairs.append(
            (
                f"{key_prefix}DefaultNetworkCardIndex",
                str(value["default_network_card_index"]),
            )
        )
    if "network_cards" in value:
        import capo_ec2.types.network_card_info_list

        capo_ec2.types.network_card_info_list.serialize_ec2_query(
            value["network_cards"], pairs, f"{key_prefix}NetworkCards"
        )
    if "ipv4_addresses_per_interface" in value:
        pairs.append(
            (
                f"{key_prefix}Ipv4AddressesPerInterface",
                str(value["ipv4_addresses_per_interface"]),
            )
        )
    if "ipv6_addresses_per_interface" in value:
        pairs.append(
            (
                f"{key_prefix}Ipv6AddressesPerInterface",
                str(value["ipv6_addresses_per_interface"]),
            )
        )
    if "ipv6_supported" in value:
        pairs.append(
            (
                f"{key_prefix}Ipv6Supported",
                "true" if value["ipv6_supported"] else "false",
            )
        )
    if "ena_support" in value:
        import capo_ec2.types.ena_support

        capo_ec2.types.ena_support.serialize_ec2_query(
            value["ena_support"], pairs, f"{key_prefix}EnaSupport"
        )
    if "efa_supported" in value:
        pairs.append(
            (f"{key_prefix}EfaSupported", "true" if value["efa_supported"] else "false")
        )
    if "efa_info" in value:
        import capo_ec2.types.efa_info

        capo_ec2.types.efa_info.serialize_ec2_query(
            value["efa_info"], pairs, f"{key_prefix}EfaInfo"
        )
    if "encryption_in_transit_supported" in value:
        pairs.append(
            (
                f"{key_prefix}EncryptionInTransitSupported",
                "true" if value["encryption_in_transit_supported"] else "false",
            )
        )
    if "ena_srd_supported" in value:
        pairs.append(
            (
                f"{key_prefix}EnaSrdSupported",
                "true" if value["ena_srd_supported"] else "false",
            )
        )
    if "bandwidth_weightings" in value:
        import capo_ec2.types.bandwidth_weighting_type_list

        capo_ec2.types.bandwidth_weighting_type_list.serialize_ec2_query(
            value["bandwidth_weightings"], pairs, f"{key_prefix}BandwidthWeightings"
        )
    if "flexible_ena_queues_support" in value:
        import capo_ec2.types.flexible_ena_queues_support

        capo_ec2.types.flexible_ena_queues_support.serialize_ec2_query(
            value["flexible_ena_queues_support"],
            pairs,
            f"{key_prefix}FlexibleEnaQueuesSupport",
        )
    if "connection_tracking_configuration" in value:
        import capo_ec2.types.default_connection_tracking_configuration

        capo_ec2.types.default_connection_tracking_configuration.serialize_ec2_query(
            value["connection_tracking_configuration"],
            pairs,
            f"{key_prefix}ConnectionTrackingConfiguration",
        )
    if "secondary_network_supported" in value:
        pairs.append(
            (
                f"{key_prefix}SecondaryNetworkSupported",
                "true" if value["secondary_network_supported"] else "false",
            )
        )
    if "maximum_secondary_network_interfaces" in value:
        pairs.append(
            (
                f"{key_prefix}MaximumSecondaryNetworkInterfaces",
                str(value["maximum_secondary_network_interfaces"]),
            )
        )
    if "ipv4_addresses_per_secondary_interface" in value:
        pairs.append(
            (
                f"{key_prefix}Ipv4AddressesPerSecondaryInterface",
                str(value["ipv4_addresses_per_secondary_interface"]),
            )
        )


def deserialize_ec2_query(el: Element) -> NetworkInfo:
    out: NetworkInfo = {}  # type: ignore[typeddict-item]
    child_network_performance = el.find("networkPerformance")
    if child_network_performance is not None:
        out["network_performance"] = str(child_network_performance.text or "")
    child_maximum_network_interfaces = el.find("maximumNetworkInterfaces")
    if child_maximum_network_interfaces is not None:
        out["maximum_network_interfaces"] = int(
            child_maximum_network_interfaces.text or ""
        )
    child_maximum_network_cards = el.find("maximumNetworkCards")
    if child_maximum_network_cards is not None:
        out["maximum_network_cards"] = int(child_maximum_network_cards.text or "")
    child_default_network_card_index = el.find("defaultNetworkCardIndex")
    if child_default_network_card_index is not None:
        out["default_network_card_index"] = int(
            child_default_network_card_index.text or ""
        )
    child_network_cards = el.find("networkCards")
    if child_network_cards is not None:
        import capo_ec2.types.network_card_info_list

        out["network_cards"] = (
            capo_ec2.types.network_card_info_list.deserialize_ec2_query(
                child_network_cards
            )
        )
    child_ipv4_addresses_per_interface = el.find("ipv4AddressesPerInterface")
    if child_ipv4_addresses_per_interface is not None:
        out["ipv4_addresses_per_interface"] = int(
            child_ipv4_addresses_per_interface.text or ""
        )
    child_ipv6_addresses_per_interface = el.find("ipv6AddressesPerInterface")
    if child_ipv6_addresses_per_interface is not None:
        out["ipv6_addresses_per_interface"] = int(
            child_ipv6_addresses_per_interface.text or ""
        )
    child_ipv6_supported = el.find("ipv6Supported")
    if child_ipv6_supported is not None:
        out["ipv6_supported"] = (child_ipv6_supported.text or "").lower() == "true"
    child_ena_support = el.find("enaSupport")
    if child_ena_support is not None:
        import capo_ec2.types.ena_support

        out["ena_support"] = capo_ec2.types.ena_support.deserialize_ec2_query(
            child_ena_support
        )
    child_efa_supported = el.find("efaSupported")
    if child_efa_supported is not None:
        out["efa_supported"] = (child_efa_supported.text or "").lower() == "true"
    child_efa_info = el.find("efaInfo")
    if child_efa_info is not None:
        import capo_ec2.types.efa_info

        out["efa_info"] = capo_ec2.types.efa_info.deserialize_ec2_query(child_efa_info)
    child_encryption_in_transit_supported = el.find("encryptionInTransitSupported")
    if child_encryption_in_transit_supported is not None:
        out["encryption_in_transit_supported"] = (
            child_encryption_in_transit_supported.text or ""
        ).lower() == "true"
    child_ena_srd_supported = el.find("enaSrdSupported")
    if child_ena_srd_supported is not None:
        out["ena_srd_supported"] = (
            child_ena_srd_supported.text or ""
        ).lower() == "true"
    child_bandwidth_weightings = el.find("bandwidthWeightings")
    if child_bandwidth_weightings is not None:
        import capo_ec2.types.bandwidth_weighting_type_list

        out["bandwidth_weightings"] = (
            capo_ec2.types.bandwidth_weighting_type_list.deserialize_ec2_query(
                child_bandwidth_weightings
            )
        )
    child_flexible_ena_queues_support = el.find("flexibleEnaQueuesSupport")
    if child_flexible_ena_queues_support is not None:
        import capo_ec2.types.flexible_ena_queues_support

        out["flexible_ena_queues_support"] = (
            capo_ec2.types.flexible_ena_queues_support.deserialize_ec2_query(
                child_flexible_ena_queues_support
            )
        )
    child_connection_tracking_configuration = el.find("connectionTrackingConfiguration")
    if child_connection_tracking_configuration is not None:
        import capo_ec2.types.default_connection_tracking_configuration

        out["connection_tracking_configuration"] = (
            capo_ec2.types.default_connection_tracking_configuration.deserialize_ec2_query(
                child_connection_tracking_configuration
            )
        )
    child_secondary_network_supported = el.find("secondaryNetworkSupported")
    if child_secondary_network_supported is not None:
        out["secondary_network_supported"] = (
            child_secondary_network_supported.text or ""
        ).lower() == "true"
    child_maximum_secondary_network_interfaces = el.find(
        "maximumSecondaryNetworkInterfaces"
    )
    if child_maximum_secondary_network_interfaces is not None:
        out["maximum_secondary_network_interfaces"] = int(
            child_maximum_secondary_network_interfaces.text or ""
        )
    child_ipv4_addresses_per_secondary_interface = el.find(
        "ipv4AddressesPerSecondaryInterface"
    )
    if child_ipv4_addresses_per_secondary_interface is not None:
        out["ipv4_addresses_per_secondary_interface"] = int(
            child_ipv4_addresses_per_secondary_interface.text or ""
        )
    return out
