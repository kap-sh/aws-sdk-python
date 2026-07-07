"""Generated from Smithy shape ``com.amazonaws.networkmonitor#Probe``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_networkmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_networkmonitor.types.address_family
    import aws_sdk_networkmonitor.types.arn
    import aws_sdk_networkmonitor.types.destination
    import aws_sdk_networkmonitor.types.iso8601_timestamp
    import aws_sdk_networkmonitor.types.packet_size
    import aws_sdk_networkmonitor.types.port
    import aws_sdk_networkmonitor.types.probe_id
    import aws_sdk_networkmonitor.types.probe_state
    import aws_sdk_networkmonitor.types.protocol
    import aws_sdk_networkmonitor.types.tag_map
    import aws_sdk_networkmonitor.types.vpc_id


class Probe(TypedDict, closed=True):
    probe_id: NotRequired["aws_sdk_networkmonitor.types.probe_id.ProbeId"]
    """<p>The ID of the probe.</p>"""
    probe_arn: NotRequired["aws_sdk_networkmonitor.types.arn.Arn"]
    """<p>The ARN of the probe.</p>"""
    source_arn: "aws_sdk_networkmonitor.types.arn.Arn"
    """<p>The ARN of the probe source subnet.</p>"""
    destination: "aws_sdk_networkmonitor.types.destination.Destination"
    """<p>The destination for the probe. This should be either an <code>IPV4</code> or <code>IPV6</code>.</p>"""
    destination_port: NotRequired["aws_sdk_networkmonitor.types.port.Port"]
    """<p>The destination port for the probe. This is required only if the <code>protocol</code> is <code>TCP</code> and must be a number between <code>1</code> and <code>65536</code>.</p>"""
    protocol: "aws_sdk_networkmonitor.types.protocol.Protocol"
    """<p>The network protocol for the destination. This can be either <code>TCP</code> or <code>ICMP</code>. If the protocol is <code>TCP</code>, then <code>port</code> is also required.</p>"""
    packet_size: NotRequired["aws_sdk_networkmonitor.types.packet_size.PacketSize"]
    """<p>The size of the packets traveling between the <code>source</code> and <code>destination</code>. This must be a number between <code>56</code> and </p>"""
    address_family: NotRequired[
        "aws_sdk_networkmonitor.types.address_family.AddressFamily"
    ]
    """<p>The IPv4 or IPv6 address for the probe.</p>"""
    vpc_id: NotRequired["aws_sdk_networkmonitor.types.vpc_id.VpcId"]
    """<p>The ID of the source VPC subnet.</p>"""
    state: NotRequired["aws_sdk_networkmonitor.types.probe_state.ProbeState"]
    """<p>The state of the probe.</p>"""
    created_at: NotRequired[
        "aws_sdk_networkmonitor.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time and date the probe was created.</p>"""
    modified_at: NotRequired[
        "aws_sdk_networkmonitor.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time and date that the probe was last modified.</p>"""
    tags: NotRequired["aws_sdk_networkmonitor.types.tag_map.TagMap"]
    """<p>The list of key-value pairs created and assigned to the probe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Probe) -> dict:
    out: dict = {}
    if "probe_id" in value:
        out["probeId"] = value["probe_id"]
    if "probe_arn" in value:
        out["probeArn"] = value["probe_arn"]
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
    if "address_family" in value:
        import aws_sdk_networkmonitor.types.address_family

        out["addressFamily"] = (
            aws_sdk_networkmonitor.types.address_family.serialize_json(
                value["address_family"]
            )
        )
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    if "state" in value:
        import aws_sdk_networkmonitor.types.probe_state

        out["state"] = aws_sdk_networkmonitor.types.probe_state.serialize_json(
            value["state"]
        )
    if "created_at" in value:
        import aws_sdk_networkmonitor.types.iso8601_timestamp

        out["createdAt"] = (
            aws_sdk_networkmonitor.types.iso8601_timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "modified_at" in value:
        import aws_sdk_networkmonitor.types.iso8601_timestamp

        out["modifiedAt"] = (
            aws_sdk_networkmonitor.types.iso8601_timestamp.serialize_json(
                value["modified_at"]
            )
        )
    if "tags" in value:
        import aws_sdk_networkmonitor.types.tag_map

        out["tags"] = aws_sdk_networkmonitor.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> Probe:
    out: Probe = {}  # type: ignore[typeddict-item]
    if "probeId" in data:
        out["probe_id"] = data["probeId"]
    if "probeArn" in data:
        out["probe_arn"] = data["probeArn"]
    if "sourceArn" in data:
        out["source_arn"] = data["sourceArn"]
    else:
        raise DeserializationError("Probe.source_arn required")
    if "destination" in data:
        out["destination"] = data["destination"]
    else:
        raise DeserializationError("Probe.destination required")
    if "destinationPort" in data:
        out["destination_port"] = data["destinationPort"]
    if "protocol" in data:
        import aws_sdk_networkmonitor.types.protocol

        out["protocol"] = aws_sdk_networkmonitor.types.protocol.deserialize_json(
            data["protocol"]
        )
    else:
        raise DeserializationError("Probe.protocol required")
    if "packetSize" in data:
        out["packet_size"] = data["packetSize"]
    if "addressFamily" in data:
        import aws_sdk_networkmonitor.types.address_family

        out["address_family"] = (
            aws_sdk_networkmonitor.types.address_family.deserialize_json(
                data["addressFamily"]
            )
        )
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    if "state" in data:
        import aws_sdk_networkmonitor.types.probe_state

        out["state"] = aws_sdk_networkmonitor.types.probe_state.deserialize_json(
            data["state"]
        )
    if "createdAt" in data:
        import aws_sdk_networkmonitor.types.iso8601_timestamp

        out["created_at"] = (
            aws_sdk_networkmonitor.types.iso8601_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "modifiedAt" in data:
        import aws_sdk_networkmonitor.types.iso8601_timestamp

        out["modified_at"] = (
            aws_sdk_networkmonitor.types.iso8601_timestamp.deserialize_json(
                data["modifiedAt"]
            )
        )
    if "tags" in data:
        import aws_sdk_networkmonitor.types.tag_map

        out["tags"] = aws_sdk_networkmonitor.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
