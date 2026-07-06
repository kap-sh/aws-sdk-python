"""Generated from Smithy shape ``com.amazonaws.ec2#AnalysisPacketHeader``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ip_address_list
    import aws_sdk_ec2.types.port_range_list
    import aws_sdk_ec2.types.string


class AnalysisPacketHeader(TypedDict, closed=True):
    destination_addresses: NotRequired[
        "aws_sdk_ec2.types.ip_address_list.IpAddressList"
    ]
    """<p>The destination addresses.</p>"""
    destination_port_ranges: NotRequired[
        "aws_sdk_ec2.types.port_range_list.PortRangeList"
    ]
    """<p>The destination port ranges.</p>"""
    protocol: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The protocol.</p>"""
    source_addresses: NotRequired["aws_sdk_ec2.types.ip_address_list.IpAddressList"]
    """<p>The source addresses.</p>"""
    source_port_ranges: NotRequired["aws_sdk_ec2.types.port_range_list.PortRangeList"]
    """<p>The source port ranges.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AnalysisPacketHeader, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "destination_addresses" in value:
        import aws_sdk_ec2.types.ip_address_list

        aws_sdk_ec2.types.ip_address_list.serialize_ec2_query(
            value["destination_addresses"], pairs, f"{prefix}.DestinationAddressSet"
        )
    if "destination_port_ranges" in value:
        import aws_sdk_ec2.types.port_range_list

        aws_sdk_ec2.types.port_range_list.serialize_ec2_query(
            value["destination_port_ranges"], pairs, f"{prefix}.DestinationPortRangeSet"
        )
    if "protocol" in value:
        pairs.append((f"{prefix}.Protocol", str(value["protocol"])))
    if "source_addresses" in value:
        import aws_sdk_ec2.types.ip_address_list

        aws_sdk_ec2.types.ip_address_list.serialize_ec2_query(
            value["source_addresses"], pairs, f"{prefix}.SourceAddressSet"
        )
    if "source_port_ranges" in value:
        import aws_sdk_ec2.types.port_range_list

        aws_sdk_ec2.types.port_range_list.serialize_ec2_query(
            value["source_port_ranges"], pairs, f"{prefix}.SourcePortRangeSet"
        )


def deserialize_ec2_query(el: Element) -> AnalysisPacketHeader:
    out: AnalysisPacketHeader = {}  # type: ignore[typeddict-item]
    if el.find("DestinationAddressSet") is not None:
        import aws_sdk_ec2.types.ip_address_list

        out["destination_addresses"] = (
            aws_sdk_ec2.types.ip_address_list.deserialize_ec2_query(
                el, "DestinationAddressSet"
            )
        )
    if el.find("DestinationPortRangeSet") is not None:
        import aws_sdk_ec2.types.port_range_list

        out["destination_port_ranges"] = (
            aws_sdk_ec2.types.port_range_list.deserialize_ec2_query(
                el, "DestinationPortRangeSet"
            )
        )
    child_protocol = el.find("Protocol")
    if child_protocol is not None:
        out["protocol"] = str(child_protocol.text or "")
    if el.find("SourceAddressSet") is not None:
        import aws_sdk_ec2.types.ip_address_list

        out["source_addresses"] = (
            aws_sdk_ec2.types.ip_address_list.deserialize_ec2_query(
                el, "SourceAddressSet"
            )
        )
    if el.find("SourcePortRangeSet") is not None:
        import aws_sdk_ec2.types.port_range_list

        out["source_port_ranges"] = (
            aws_sdk_ec2.types.port_range_list.deserialize_ec2_query(
                el, "SourcePortRangeSet"
            )
        )
    return out
