"""Generated from Smithy shape ``com.amazonaws.ec2#AnalysisPacketHeader``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ip_address_list
    import capo_ec2.types.port_range_list
    import capo_ec2.types.string


class AnalysisPacketHeader(TypedDict, closed=True):
    destination_addresses: NotRequired["capo_ec2.types.ip_address_list.IpAddressList"]
    """<p>The destination addresses.</p>"""
    destination_port_ranges: NotRequired["capo_ec2.types.port_range_list.PortRangeList"]
    """<p>The destination port ranges.</p>"""
    protocol: NotRequired["capo_ec2.types.string.String"]
    """<p>The protocol.</p>"""
    source_addresses: NotRequired["capo_ec2.types.ip_address_list.IpAddressList"]
    """<p>The source addresses.</p>"""
    source_port_ranges: NotRequired["capo_ec2.types.port_range_list.PortRangeList"]
    """<p>The source port ranges.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AnalysisPacketHeader, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "destination_addresses" in value:
        import capo_ec2.types.ip_address_list

        capo_ec2.types.ip_address_list.serialize_ec2_query(
            value["destination_addresses"], pairs, f"{key_prefix}DestinationAddressSet"
        )
    if "destination_port_ranges" in value:
        import capo_ec2.types.port_range_list

        capo_ec2.types.port_range_list.serialize_ec2_query(
            value["destination_port_ranges"],
            pairs,
            f"{key_prefix}DestinationPortRangeSet",
        )
    if "protocol" in value:
        pairs.append((f"{key_prefix}Protocol", str(value["protocol"])))
    if "source_addresses" in value:
        import capo_ec2.types.ip_address_list

        capo_ec2.types.ip_address_list.serialize_ec2_query(
            value["source_addresses"], pairs, f"{key_prefix}SourceAddressSet"
        )
    if "source_port_ranges" in value:
        import capo_ec2.types.port_range_list

        capo_ec2.types.port_range_list.serialize_ec2_query(
            value["source_port_ranges"], pairs, f"{key_prefix}SourcePortRangeSet"
        )


def deserialize_ec2_query(el: Element) -> AnalysisPacketHeader:
    out: AnalysisPacketHeader = {}  # type: ignore[typeddict-item]
    child_destination_addresses = el.find("destinationAddressSet")
    if child_destination_addresses is not None:
        import capo_ec2.types.ip_address_list

        out["destination_addresses"] = (
            capo_ec2.types.ip_address_list.deserialize_ec2_query(
                child_destination_addresses
            )
        )
    child_destination_port_ranges = el.find("destinationPortRangeSet")
    if child_destination_port_ranges is not None:
        import capo_ec2.types.port_range_list

        out["destination_port_ranges"] = (
            capo_ec2.types.port_range_list.deserialize_ec2_query(
                child_destination_port_ranges
            )
        )
    child_protocol = el.find("protocol")
    if child_protocol is not None:
        out["protocol"] = str(child_protocol.text or "")
    child_source_addresses = el.find("sourceAddressSet")
    if child_source_addresses is not None:
        import capo_ec2.types.ip_address_list

        out["source_addresses"] = capo_ec2.types.ip_address_list.deserialize_ec2_query(
            child_source_addresses
        )
    child_source_port_ranges = el.find("sourcePortRangeSet")
    if child_source_port_ranges is not None:
        import capo_ec2.types.port_range_list

        out["source_port_ranges"] = (
            capo_ec2.types.port_range_list.deserialize_ec2_query(
                child_source_port_ranges
            )
        )
    return out
