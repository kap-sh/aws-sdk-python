"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UpdateBridgeNetworkOutputRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.protocol


class UpdateBridgeNetworkOutputRequest(TypedDict, closed=True):
    ip_address: NotRequired["str"]
    """<p>The network output IP Address. </p>"""
    network_name: NotRequired["str"]
    """<p>The network output's gateway network name. </p>"""
    port: NotRequired["int"]
    """<p>The network output port. </p>"""
    protocol: NotRequired["aws_sdk_mediaconnect.types.protocol.Protocol"]
    """<p>The network output protocol. </p> <note> <p>Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.</p> </note>"""
    ttl: NotRequired["int"]
    """<p>The network output TTL. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBridgeNetworkOutputRequest) -> dict:
    out: dict = {}
    if "ip_address" in value:
        out["ipAddress"] = value["ip_address"]
    if "network_name" in value:
        out["networkName"] = value["network_name"]
    if "port" in value:
        out["port"] = value["port"]
    if "protocol" in value:
        import aws_sdk_mediaconnect.types.protocol

        out["protocol"] = aws_sdk_mediaconnect.types.protocol.serialize_json(
            value["protocol"]
        )
    if "ttl" in value:
        out["ttl"] = value["ttl"]
    return out


def deserialize_json(data: dict) -> UpdateBridgeNetworkOutputRequest:
    out: UpdateBridgeNetworkOutputRequest = {}  # type: ignore[typeddict-item]
    if "ipAddress" in data:
        out["ip_address"] = data["ipAddress"]
    if "networkName" in data:
        out["network_name"] = data["networkName"]
    if "port" in data:
        out["port"] = data["port"]
    if "protocol" in data:
        import aws_sdk_mediaconnect.types.protocol

        out["protocol"] = aws_sdk_mediaconnect.types.protocol.deserialize_json(
            data["protocol"]
        )
    if "ttl" in data:
        out["ttl"] = data["ttl"]
    return out
