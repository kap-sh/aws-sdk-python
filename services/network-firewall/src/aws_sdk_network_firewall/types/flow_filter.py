"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FlowFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.address
    import aws_sdk_network_firewall.types.port
    import aws_sdk_network_firewall.types.protocol_strings


class FlowFilter(TypedDict, closed=True):
    source_address: NotRequired["aws_sdk_network_firewall.types.address.Address"]
    destination_address: NotRequired["aws_sdk_network_firewall.types.address.Address"]
    source_port: NotRequired["aws_sdk_network_firewall.types.port.Port"]
    """<p>The source port to inspect for. You can specify an individual port, for example <code>1994</code> and you can specify a port range, for example <code>1990:1994</code>. To match with any port, specify <code>ANY</code>.</p>"""
    destination_port: NotRequired["aws_sdk_network_firewall.types.port.Port"]
    """<p>The destination port to inspect for. You can specify an individual port, for example <code>1994</code> and you can specify a port range, for example <code>1990:1994</code>. To match with any port, specify <code>ANY</code>.</p>"""
    protocols: NotRequired[
        "aws_sdk_network_firewall.types.protocol_strings.ProtocolStrings"
    ]
    """<p>The protocols to inspect for, specified using the assigned internet protocol number (IANA) for each protocol. If not specified, this matches with any protocol.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FlowFilter) -> dict:
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
    if "protocols" in value:
        import aws_sdk_network_firewall.types.protocol_strings

        out["Protocols"] = (
            aws_sdk_network_firewall.types.protocol_strings.serialize_aws_json_1_0(
                value["protocols"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> FlowFilter:
    out: FlowFilter = {}  # type: ignore[typeddict-item]
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
    if "Protocols" in data:
        import aws_sdk_network_firewall.types.protocol_strings

        out["protocols"] = (
            aws_sdk_network_firewall.types.protocol_strings.deserialize_aws_json_1_0(
                data["Protocols"]
            )
        )
    return out
