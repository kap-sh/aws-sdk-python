"""Generated from Smithy shape ``com.amazonaws.guardduty#NetworkConnectionAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.boolean
    import capo_guardduty.types.local_ip_details
    import capo_guardduty.types.local_port_details
    import capo_guardduty.types.remote_ip_details
    import capo_guardduty.types.remote_port_details
    import capo_guardduty.types.string


class NetworkConnectionAction(TypedDict, closed=True):
    blocked: NotRequired["capo_guardduty.types.boolean.Boolean"]
    """<p>Indicates whether EC2 blocked the network connection to your instance.</p>"""
    connection_direction: NotRequired["capo_guardduty.types.string.String"]
    """<p>The network connection direction.</p>"""
    local_port_details: NotRequired[
        "capo_guardduty.types.local_port_details.LocalPortDetails"
    ]
    """<p>The local port information of the connection.</p>"""
    protocol: NotRequired["capo_guardduty.types.string.String"]
    """<p>The network connection protocol.</p>"""
    local_ip_details: NotRequired[
        "capo_guardduty.types.local_ip_details.LocalIpDetails"
    ]
    """<p>The local IP information of the connection.</p>"""
    local_network_interface: NotRequired["capo_guardduty.types.string.String"]
    """<p>The EC2 instance's local elastic network interface utilized for the connection.</p>"""
    remote_ip_details: NotRequired[
        "capo_guardduty.types.remote_ip_details.RemoteIpDetails"
    ]
    """<p>The remote IP information of the connection.</p>"""
    remote_port_details: NotRequired[
        "capo_guardduty.types.remote_port_details.RemotePortDetails"
    ]
    """<p>The remote port information of the connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkConnectionAction) -> dict:
    out: dict = {}
    if "blocked" in value:
        out["blocked"] = value["blocked"]
    if "connection_direction" in value:
        out["connectionDirection"] = value["connection_direction"]
    if "local_port_details" in value:
        import capo_guardduty.types.local_port_details

        out["localPortDetails"] = (
            capo_guardduty.types.local_port_details.serialize_json(
                value["local_port_details"]
            )
        )
    if "protocol" in value:
        out["protocol"] = value["protocol"]
    if "local_ip_details" in value:
        import capo_guardduty.types.local_ip_details

        out["localIpDetails"] = capo_guardduty.types.local_ip_details.serialize_json(
            value["local_ip_details"]
        )
    if "local_network_interface" in value:
        out["localNetworkInterface"] = value["local_network_interface"]
    if "remote_ip_details" in value:
        import capo_guardduty.types.remote_ip_details

        out["remoteIpDetails"] = capo_guardduty.types.remote_ip_details.serialize_json(
            value["remote_ip_details"]
        )
    if "remote_port_details" in value:
        import capo_guardduty.types.remote_port_details

        out["remotePortDetails"] = (
            capo_guardduty.types.remote_port_details.serialize_json(
                value["remote_port_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> NetworkConnectionAction:
    out: NetworkConnectionAction = {}  # type: ignore[typeddict-item]
    if "blocked" in data:
        out["blocked"] = data["blocked"]
    if "connectionDirection" in data:
        out["connection_direction"] = data["connectionDirection"]
    if "localPortDetails" in data:
        import capo_guardduty.types.local_port_details

        out["local_port_details"] = (
            capo_guardduty.types.local_port_details.deserialize_json(
                data["localPortDetails"]
            )
        )
    if "protocol" in data:
        out["protocol"] = data["protocol"]
    if "localIpDetails" in data:
        import capo_guardduty.types.local_ip_details

        out["local_ip_details"] = (
            capo_guardduty.types.local_ip_details.deserialize_json(
                data["localIpDetails"]
            )
        )
    if "localNetworkInterface" in data:
        out["local_network_interface"] = data["localNetworkInterface"]
    if "remoteIpDetails" in data:
        import capo_guardduty.types.remote_ip_details

        out["remote_ip_details"] = (
            capo_guardduty.types.remote_ip_details.deserialize_json(
                data["remoteIpDetails"]
            )
        )
    if "remotePortDetails" in data:
        import capo_guardduty.types.remote_port_details

        out["remote_port_details"] = (
            capo_guardduty.types.remote_port_details.deserialize_json(
                data["remotePortDetails"]
            )
        )
    return out
