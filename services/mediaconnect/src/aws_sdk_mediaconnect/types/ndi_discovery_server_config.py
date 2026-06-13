"""Generated from Smithy shape ``com.amazonaws.mediaconnect#NdiDiscoveryServerConfig``."""

from typing import TypedDict

from typing_extensions import NotRequired


class NdiDiscoveryServerConfig(TypedDict):
    discovery_server_address: NotRequired["str"]
    """<p>The unique network address of the NDI discovery server. </p>"""
    discovery_server_port: NotRequired["int"]
    """<p>The port for the NDI discovery server. Defaults to 5959 if a custom port isn't specified. </p>"""
    vpc_interface_adapter: NotRequired["str"]
    """<p>The identifier for the Virtual Private Cloud (VPC) network interface used by the flow. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NdiDiscoveryServerConfig) -> dict:
    out: dict = {}
    if "discovery_server_address" in value:
        out["discoveryServerAddress"] = value["discovery_server_address"]
    if "discovery_server_port" in value:
        out["discoveryServerPort"] = value["discovery_server_port"]
    if "vpc_interface_adapter" in value:
        out["vpcInterfaceAdapter"] = value["vpc_interface_adapter"]
    return out


def deserialize_json(data: dict) -> NdiDiscoveryServerConfig:
    out: NdiDiscoveryServerConfig = {}  # type: ignore[typeddict-item]
    if "discoveryServerAddress" in data:
        out["discovery_server_address"] = data["discoveryServerAddress"]
    if "discoveryServerPort" in data:
        out["discovery_server_port"] = data["discoveryServerPort"]
    if "vpcInterfaceAdapter" in data:
        out["vpc_interface_adapter"] = data["vpcInterfaceAdapter"]
    return out
