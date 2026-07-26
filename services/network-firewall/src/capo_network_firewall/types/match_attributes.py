"""Generated from Smithy shape ``com.amazonaws.networkfirewall#MatchAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.addresses
    import capo_network_firewall.types.port_ranges
    import capo_network_firewall.types.protocol_numbers
    import capo_network_firewall.types.tcp_flags


class MatchAttributes(TypedDict, closed=True):
    sources: NotRequired["capo_network_firewall.types.addresses.Addresses"]
    """<p>The source IP addresses and address ranges to inspect for, in CIDR notation. If not specified, this matches with any source address. </p>"""
    destinations: NotRequired["capo_network_firewall.types.addresses.Addresses"]
    """<p>The destination IP addresses and address ranges to inspect for, in CIDR notation. If not specified, this matches with any destination address. </p>"""
    source_ports: NotRequired["capo_network_firewall.types.port_ranges.PortRanges"]
    """<p>The source port to inspect for. You can specify an individual port, for example <code>1994</code> and you can specify a port range, for example <code>1990:1994</code>. To match with any port, specify <code>ANY</code>.</p> <p> If not specified, this matches with any source port.</p> <p>This setting is only used for protocols 6 (TCP) and 17 (UDP).</p>"""
    destination_ports: NotRequired["capo_network_firewall.types.port_ranges.PortRanges"]
    """<p>The destination port to inspect for. You can specify an individual port, for example <code>1994</code> and you can specify a port range, for example <code>1990:1994</code>. To match with any port, specify <code>ANY</code>.</p> <p>This setting is only used for protocols 6 (TCP) and 17 (UDP). </p>"""
    protocols: NotRequired[
        "capo_network_firewall.types.protocol_numbers.ProtocolNumbers"
    ]
    """<p>The protocols to inspect for, specified using the assigned internet protocol number (IANA) for each protocol. If not specified, this matches with any protocol.</p>"""
    tcp_flags: NotRequired["capo_network_firewall.types.tcp_flags.TCPFlags"]
    """<p>The TCP flags and masks to inspect for. If not specified, this matches with any settings. This setting is only used for protocol 6 (TCP).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MatchAttributes) -> dict:
    out: dict = {}
    if "sources" in value:
        import capo_network_firewall.types.addresses

        out["Sources"] = capo_network_firewall.types.addresses.serialize_aws_json_1_0(
            value["sources"]
        )
    if "destinations" in value:
        import capo_network_firewall.types.addresses

        out["Destinations"] = (
            capo_network_firewall.types.addresses.serialize_aws_json_1_0(
                value["destinations"]
            )
        )
    if "source_ports" in value:
        import capo_network_firewall.types.port_ranges

        out["SourcePorts"] = (
            capo_network_firewall.types.port_ranges.serialize_aws_json_1_0(
                value["source_ports"]
            )
        )
    if "destination_ports" in value:
        import capo_network_firewall.types.port_ranges

        out["DestinationPorts"] = (
            capo_network_firewall.types.port_ranges.serialize_aws_json_1_0(
                value["destination_ports"]
            )
        )
    if "protocols" in value:
        import capo_network_firewall.types.protocol_numbers

        out["Protocols"] = (
            capo_network_firewall.types.protocol_numbers.serialize_aws_json_1_0(
                value["protocols"]
            )
        )
    if "tcp_flags" in value:
        import capo_network_firewall.types.tcp_flags

        out["TCPFlags"] = capo_network_firewall.types.tcp_flags.serialize_aws_json_1_0(
            value["tcp_flags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> MatchAttributes:
    out: MatchAttributes = {}  # type: ignore[typeddict-item]
    if "Sources" in data:
        import capo_network_firewall.types.addresses

        out["sources"] = capo_network_firewall.types.addresses.deserialize_aws_json_1_0(
            data["Sources"]
        )
    if "Destinations" in data:
        import capo_network_firewall.types.addresses

        out["destinations"] = (
            capo_network_firewall.types.addresses.deserialize_aws_json_1_0(
                data["Destinations"]
            )
        )
    if "SourcePorts" in data:
        import capo_network_firewall.types.port_ranges

        out["source_ports"] = (
            capo_network_firewall.types.port_ranges.deserialize_aws_json_1_0(
                data["SourcePorts"]
            )
        )
    if "DestinationPorts" in data:
        import capo_network_firewall.types.port_ranges

        out["destination_ports"] = (
            capo_network_firewall.types.port_ranges.deserialize_aws_json_1_0(
                data["DestinationPorts"]
            )
        )
    if "Protocols" in data:
        import capo_network_firewall.types.protocol_numbers

        out["protocols"] = (
            capo_network_firewall.types.protocol_numbers.deserialize_aws_json_1_0(
                data["Protocols"]
            )
        )
    if "TCPFlags" in data:
        import capo_network_firewall.types.tcp_flags

        out["tcp_flags"] = (
            capo_network_firewall.types.tcp_flags.deserialize_aws_json_1_0(
                data["TCPFlags"]
            )
        )
    return out
