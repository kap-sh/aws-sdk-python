"""Generated from Smithy shape ``com.amazonaws.mediaconnect#AddBridgeNetworkSourceRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.multicast_source_settings
    import aws_sdk_mediaconnect.types.protocol

class AddBridgeNetworkSourceRequest(TypedDict):
    multicast_ip: NotRequired["str"]
    """<p> The network source multicast IP.</p>"""
    multicast_source_settings: NotRequired["aws_sdk_mediaconnect.types.multicast_source_settings.MulticastSourceSettings"]
    """<p> The settings related to the multicast source. </p>"""
    name: NotRequired["str"]
    """<p> The name of the network source. This name is used to reference the source and must be unique among sources in this bridge.</p>"""
    network_name: NotRequired["str"]
    """<p> The network source's gateway network name.</p>"""
    port: NotRequired["int"]
    """<p> The network source port.</p>"""
    protocol: NotRequired["aws_sdk_mediaconnect.types.protocol.Protocol"]
    """<p> The network source protocol.</p> <note> <p>Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.</p> </note>"""

# --- restJson1 ser/de ---
def serialize_json(value: AddBridgeNetworkSourceRequest) -> dict:
    out: dict = {}
    if "multicast_ip" in value:
        out["multicastIp"] = value["multicast_ip"]
    if "multicast_source_settings" in value:
        import aws_sdk_mediaconnect.types.multicast_source_settings
        out["multicastSourceSettings"] = aws_sdk_mediaconnect.types.multicast_source_settings.serialize_json(value["multicast_source_settings"])
    if "name" in value:
        out["name"] = value["name"]
    if "network_name" in value:
        out["networkName"] = value["network_name"]
    if "port" in value:
        out["port"] = value["port"]
    if "protocol" in value:
        import aws_sdk_mediaconnect.types.protocol
        out["protocol"] = aws_sdk_mediaconnect.types.protocol.serialize_json(value["protocol"])
    return out


def deserialize_json(data: dict) -> AddBridgeNetworkSourceRequest:
    out: AddBridgeNetworkSourceRequest = {}  # type: ignore[typeddict-item]
    if "multicastIp" in data:
        out["multicast_ip"] = data["multicastIp"]
    if "multicastSourceSettings" in data:
        import aws_sdk_mediaconnect.types.multicast_source_settings
        out["multicast_source_settings"] = aws_sdk_mediaconnect.types.multicast_source_settings.deserialize_json(data["multicastSourceSettings"])
    if "name" in data:
        out["name"] = data["name"]
    if "networkName" in data:
        out["network_name"] = data["networkName"]
    if "port" in data:
        out["port"] = data["port"]
    if "protocol" in data:
        import aws_sdk_mediaconnect.types.protocol
        out["protocol"] = aws_sdk_mediaconnect.types.protocol.deserialize_json(data["protocol"])
    return out