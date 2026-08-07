"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#SetSubnetsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.availability_zones
    import capo_elastic_load_balancing_v2.types.enable_prefix_for_ipv6_source_nat_enum
    import capo_elastic_load_balancing_v2.types.ip_address_type


class SetSubnetsOutput(TypedDict, closed=True):
    availability_zones: NotRequired[
        "capo_elastic_load_balancing_v2.types.availability_zones.AvailabilityZones"
    ]
    """<p>Information about the subnets.</p>"""
    ip_address_type: NotRequired[
        "capo_elastic_load_balancing_v2.types.ip_address_type.IpAddressType"
    ]
    """<p>The IP address type.</p>"""
    enable_prefix_for_ipv6_source_nat: NotRequired[
        "capo_elastic_load_balancing_v2.types.enable_prefix_for_ipv6_source_nat_enum.EnablePrefixForIpv6SourceNatEnum"
    ]
    """<p>[Network Load Balancers] Indicates whether to use an IPv6 prefix from each subnet for source NAT.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SetSubnetsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "availability_zones" in value:
        import capo_elastic_load_balancing_v2.types.availability_zones

        capo_elastic_load_balancing_v2.types.availability_zones.serialize_query(
            value["availability_zones"], pairs, f"{key_prefix}AvailabilityZones"
        )
    if "ip_address_type" in value:
        import capo_elastic_load_balancing_v2.types.ip_address_type

        capo_elastic_load_balancing_v2.types.ip_address_type.serialize_query(
            value["ip_address_type"], pairs, f"{key_prefix}IpAddressType"
        )
    if "enable_prefix_for_ipv6_source_nat" in value:
        import capo_elastic_load_balancing_v2.types.enable_prefix_for_ipv6_source_nat_enum

        capo_elastic_load_balancing_v2.types.enable_prefix_for_ipv6_source_nat_enum.serialize_query(
            value["enable_prefix_for_ipv6_source_nat"],
            pairs,
            f"{key_prefix}EnablePrefixForIpv6SourceNat",
        )


def deserialize_query(el: Element) -> SetSubnetsOutput:
    out: SetSubnetsOutput = {}  # type: ignore[typeddict-item]
    child_availability_zones = el.find("AvailabilityZones")
    if child_availability_zones is not None:
        import capo_elastic_load_balancing_v2.types.availability_zones

        out["availability_zones"] = (
            capo_elastic_load_balancing_v2.types.availability_zones.deserialize_query(
                child_availability_zones
            )
        )
    child_ip_address_type = el.find("IpAddressType")
    if child_ip_address_type is not None:
        import capo_elastic_load_balancing_v2.types.ip_address_type

        out["ip_address_type"] = (
            capo_elastic_load_balancing_v2.types.ip_address_type.deserialize_query(
                child_ip_address_type
            )
        )
    child_enable_prefix_for_ipv6_source_nat = el.find("EnablePrefixForIpv6SourceNat")
    if child_enable_prefix_for_ipv6_source_nat is not None:
        import capo_elastic_load_balancing_v2.types.enable_prefix_for_ipv6_source_nat_enum

        out["enable_prefix_for_ipv6_source_nat"] = (
            capo_elastic_load_balancing_v2.types.enable_prefix_for_ipv6_source_nat_enum.deserialize_query(
                child_enable_prefix_for_ipv6_source_nat
            )
        )
    return out
