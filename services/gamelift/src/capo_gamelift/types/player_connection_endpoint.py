"""Generated from Smithy shape ``com.amazonaws.gamelift#PlayerConnectionEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.ip_address
    import capo_gamelift.types.port_number


class PlayerConnectionEndpoint(TypedDict, closed=True):
    ip_address: NotRequired["capo_gamelift.types.ip_address.IpAddress"]
    """<p>IP address for connecting to the game session. When player gateway is enabled, this is a player gateway IP address. When player gateway is disabled, this is the game server IP address.</p>"""
    port: NotRequired["capo_gamelift.types.port_number.PortNumber"]
    """<p>Port number for connecting to the game session. When player gateway is enabled, this is a player gateway port. When player gateway is disabled, this is the game server port.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlayerConnectionEndpoint) -> dict:
    out: dict = {}
    if "ip_address" in value:
        out["IpAddress"] = value["ip_address"]
    if "port" in value:
        out["Port"] = value["port"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PlayerConnectionEndpoint:
    out: PlayerConnectionEndpoint = {}  # type: ignore[typeddict-item]
    if "IpAddress" in data:
        out["ip_address"] = data["IpAddress"]
    if "Port" in data:
        out["port"] = data["Port"]
    return out
