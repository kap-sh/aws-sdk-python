"""Generated from Smithy shape ``com.amazonaws.networkmonitor#ProbeInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_networkmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_networkmonitor.types.arn
    import aws_sdk_networkmonitor.types.destination
    import aws_sdk_networkmonitor.types.packet_size
    import aws_sdk_networkmonitor.types.port
    import aws_sdk_networkmonitor.types.protocol
    import aws_sdk_networkmonitor.types.tag_map


class ProbeInput(TypedDict):
    source_arn: "aws_sdk_networkmonitor.types.arn.Arn"
    """<p>The ARN of the subnet.</p>"""
    destination: "aws_sdk_networkmonitor.types.destination.Destination"
    """<p>The destination IP address. This must be either <code>IPV4</code> or <code>IPV6</code>.</p>"""
    destination_port: NotRequired["aws_sdk_networkmonitor.types.port.Port"]
    """<p>The port associated with the <code>destination</code>. This is required only if the <code>protocol</code> is <code>TCP</code> and must be a number between <code>1</code> and <code>65536</code>.</p>"""
    protocol: "aws_sdk_networkmonitor.types.protocol.Protocol"
    """<p>The protocol used for the network traffic between the <code>source</code> and <code>destination</code>. This must be either <code>TCP</code> or <code>ICMP</code>.</p>"""
    packet_size: NotRequired["aws_sdk_networkmonitor.types.packet_size.PacketSize"]
    """<p>The size of the packets sent between the source and destination. This must be a number between <code>56</code> and <code>8500</code>.</p>"""
    tags: NotRequired["aws_sdk_networkmonitor.types.tag_map.TagMap"]
    """<p>The list of key-value pairs created and assigned to the monitor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProbeInput) -> dict:
    out: dict = {}
    out["sourceArn"] = value["source_arn"]
    out["destination"] = value["destination"]
    if "destination_port" in value:
        out["destinationPort"] = value["destination_port"]
    import aws_sdk_networkmonitor.types.protocol

    out["protocol"] = aws_sdk_networkmonitor.types.protocol.serialize_json(
        value["protocol"]
    )
    if "packet_size" in value:
        out["packetSize"] = value["packet_size"]
    if "tags" in value:
        import aws_sdk_networkmonitor.types.tag_map

        out["tags"] = aws_sdk_networkmonitor.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ProbeInput:
    out: ProbeInput = {}  # type: ignore[typeddict-item]
    if "sourceArn" in data:
        out["source_arn"] = data["sourceArn"]
    else:
        raise DeserializationError("ProbeInput.source_arn required")
    if "destination" in data:
        out["destination"] = data["destination"]
    else:
        raise DeserializationError("ProbeInput.destination required")
    if "destinationPort" in data:
        out["destination_port"] = data["destinationPort"]
    if "protocol" in data:
        import aws_sdk_networkmonitor.types.protocol

        out["protocol"] = aws_sdk_networkmonitor.types.protocol.deserialize_json(
            data["protocol"]
        )
    else:
        raise DeserializationError("ProbeInput.protocol required")
    if "packetSize" in data:
        out["packet_size"] = data["packetSize"]
    if "tags" in data:
        import aws_sdk_networkmonitor.types.tag_map

        out["tags"] = aws_sdk_networkmonitor.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
