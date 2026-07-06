"""Generated from Smithy shape ``com.amazonaws.networkmonitor#UpdateProbeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmonitor.types.destination
    import aws_sdk_networkmonitor.types.packet_size
    import aws_sdk_networkmonitor.types.port
    import aws_sdk_networkmonitor.types.probe_id
    import aws_sdk_networkmonitor.types.probe_state
    import aws_sdk_networkmonitor.types.protocol
    import aws_sdk_networkmonitor.types.resource_name


class UpdateProbeInput(TypedDict, closed=True):
    monitor_name: "aws_sdk_networkmonitor.types.resource_name.ResourceName"
    """<p>The name of the monitor that the probe was updated for.</p>"""
    probe_id: "aws_sdk_networkmonitor.types.probe_id.ProbeId"
    """<p>The ID of the probe to update.</p>"""
    state: NotRequired["aws_sdk_networkmonitor.types.probe_state.ProbeState"]
    """<p>The state of the probe update.</p>"""
    destination: NotRequired["aws_sdk_networkmonitor.types.destination.Destination"]
    """<p>The updated IP address for the probe destination. This must be either an IPv4 or IPv6 address.</p>"""
    destination_port: NotRequired["aws_sdk_networkmonitor.types.port.Port"]
    """<p>The updated port for the probe destination. This is required only if the <code>protocol</code> is <code>TCP</code> and must be a number between <code>1</code> and <code>65536</code>.</p>"""
    protocol: NotRequired["aws_sdk_networkmonitor.types.protocol.Protocol"]
    """<p>The updated network protocol for the destination. This can be either <code>TCP</code> or <code>ICMP</code>. If the protocol is <code>TCP</code>, then <code>port</code> is also required.</p>"""
    packet_size: NotRequired["aws_sdk_networkmonitor.types.packet_size.PacketSize"]
    """<p>he updated packets size for network traffic between the source and destination. This must be a number between <code>56</code> and <code>8500</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProbeInput) -> dict:
    out: dict = {}
    if "state" in value:
        import aws_sdk_networkmonitor.types.probe_state

        out["state"] = aws_sdk_networkmonitor.types.probe_state.serialize_json(
            value["state"]
        )
    if "destination" in value:
        out["destination"] = value["destination"]
    if "destination_port" in value:
        out["destinationPort"] = value["destination_port"]
    if "protocol" in value:
        import aws_sdk_networkmonitor.types.protocol

        out["protocol"] = aws_sdk_networkmonitor.types.protocol.serialize_json(
            value["protocol"]
        )
    if "packet_size" in value:
        out["packetSize"] = value["packet_size"]
    return out


def deserialize_json(data: dict) -> UpdateProbeInput:
    out: UpdateProbeInput = {}  # type: ignore[typeddict-item]
    if "state" in data:
        import aws_sdk_networkmonitor.types.probe_state

        out["state"] = aws_sdk_networkmonitor.types.probe_state.deserialize_json(
            data["state"]
        )
    if "destination" in data:
        out["destination"] = data["destination"]
    if "destinationPort" in data:
        out["destination_port"] = data["destinationPort"]
    if "protocol" in data:
        import aws_sdk_networkmonitor.types.protocol

        out["protocol"] = aws_sdk_networkmonitor.types.protocol.deserialize_json(
            data["protocol"]
        )
    if "packetSize" in data:
        out["packet_size"] = data["packetSize"]
    return out
