"""Generated from Smithy shape ``com.amazonaws.networkfirewall#Flow``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.address
    import aws_sdk_network_firewall.types.age
    import aws_sdk_network_firewall.types.byte_count
    import aws_sdk_network_firewall.types.packet_count
    import aws_sdk_network_firewall.types.port
    import aws_sdk_network_firewall.types.protocol_string


class Flow(TypedDict, closed=True):
    source_address: NotRequired["aws_sdk_network_firewall.types.address.Address"]
    destination_address: NotRequired["aws_sdk_network_firewall.types.address.Address"]
    source_port: NotRequired["aws_sdk_network_firewall.types.port.Port"]
    """<p>The source port to inspect for. You can specify an individual port, for example <code>1994</code> and you can specify a port range, for example <code>1990:1994</code>. To match with any port, specify <code>ANY</code>.</p>"""
    destination_port: NotRequired["aws_sdk_network_firewall.types.port.Port"]
    """<p>The destination port to inspect for. You can specify an individual port, for example <code>1994</code> and you can specify a port range, for example <code>1990:1994</code>. To match with any port, specify <code>ANY</code>.</p>"""
    protocol: NotRequired[
        "aws_sdk_network_firewall.types.protocol_string.ProtocolString"
    ]
    """<p>The protocols to inspect for, specified using the assigned internet protocol number (IANA) for each protocol. If not specified, this matches with any protocol.</p>"""
    age: NotRequired["aws_sdk_network_firewall.types.age.Age"]
    """<p>Returned as info about age of the flows identified by the flow operation.</p>"""
    packet_count: NotRequired["aws_sdk_network_firewall.types.packet_count.PacketCount"]
    """<p>Returns the total number of data packets received or transmitted in a flow.</p>"""
    byte_count: "aws_sdk_network_firewall.types.byte_count.ByteCount"
    """<p>Returns the number of bytes received or transmitted in a specific flow.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Flow) -> dict:
    out: dict = {}
    if "source_address" in value:
        import aws_sdk_network_firewall.types.address

        out["SourceAddress"] = (
            aws_sdk_network_firewall.types.address.serialize_aws_json_1_0(
                value["source_address"]
            )
        )
    if "destination_address" in value:
        import aws_sdk_network_firewall.types.address

        out["DestinationAddress"] = (
            aws_sdk_network_firewall.types.address.serialize_aws_json_1_0(
                value["destination_address"]
            )
        )
    if "source_port" in value:
        out["SourcePort"] = value["source_port"]
    if "destination_port" in value:
        out["DestinationPort"] = value["destination_port"]
    if "protocol" in value:
        out["Protocol"] = value["protocol"]
    if "age" in value:
        out["Age"] = value["age"]
    if "packet_count" in value:
        out["PacketCount"] = value["packet_count"]
    out["ByteCount"] = value.get("byte_count", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> Flow:
    out: Flow = {}  # type: ignore[typeddict-item]
    if "SourceAddress" in data:
        import aws_sdk_network_firewall.types.address

        out["source_address"] = (
            aws_sdk_network_firewall.types.address.deserialize_aws_json_1_0(
                data["SourceAddress"]
            )
        )
    if "DestinationAddress" in data:
        import aws_sdk_network_firewall.types.address

        out["destination_address"] = (
            aws_sdk_network_firewall.types.address.deserialize_aws_json_1_0(
                data["DestinationAddress"]
            )
        )
    if "SourcePort" in data:
        out["source_port"] = data["SourcePort"]
    if "DestinationPort" in data:
        out["destination_port"] = data["DestinationPort"]
    if "Protocol" in data:
        out["protocol"] = data["Protocol"]
    if "Age" in data:
        out["age"] = data["Age"]
    if "PacketCount" in data:
        out["packet_count"] = data["PacketCount"]
    if "ByteCount" in data:
        out["byte_count"] = data["ByteCount"]
    else:
        out["byte_count"] = 0
    return out
