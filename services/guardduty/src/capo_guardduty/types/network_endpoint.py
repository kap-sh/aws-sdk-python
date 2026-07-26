"""Generated from Smithy shape ``com.amazonaws.guardduty#NetworkEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.autonomous_system
    import capo_guardduty.types.integer
    import capo_guardduty.types.network_connection
    import capo_guardduty.types.network_geo_location
    import capo_guardduty.types.string


class NetworkEndpoint(TypedDict, closed=True):
    id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The ID of the network endpoint.</p>"""
    ip: NotRequired["capo_guardduty.types.string.String"]
    """<p>The IP address associated with the network endpoint.</p>"""
    domain: NotRequired["capo_guardduty.types.string.String"]
    """<p>The domain information for the network endpoint.</p>"""
    port: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>The port number associated with the network endpoint.</p>"""
    location: NotRequired[
        "capo_guardduty.types.network_geo_location.NetworkGeoLocation"
    ]
    """<p>Information about the location of the network endpoint.</p>"""
    autonomous_system: NotRequired[
        "capo_guardduty.types.autonomous_system.AutonomousSystem"
    ]
    """<p>The Autonomous System (AS) of the network endpoint.</p>"""
    connection: NotRequired["capo_guardduty.types.network_connection.NetworkConnection"]
    """<p>Information about the network connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkEndpoint) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "ip" in value:
        out["ip"] = value["ip"]
    if "domain" in value:
        out["domain"] = value["domain"]
    if "port" in value:
        out["port"] = value["port"]
    if "location" in value:
        import capo_guardduty.types.network_geo_location

        out["location"] = capo_guardduty.types.network_geo_location.serialize_json(
            value["location"]
        )
    if "autonomous_system" in value:
        import capo_guardduty.types.autonomous_system

        out["autonomousSystem"] = capo_guardduty.types.autonomous_system.serialize_json(
            value["autonomous_system"]
        )
    if "connection" in value:
        import capo_guardduty.types.network_connection

        out["connection"] = capo_guardduty.types.network_connection.serialize_json(
            value["connection"]
        )
    return out


def deserialize_json(data: dict) -> NetworkEndpoint:
    out: NetworkEndpoint = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "ip" in data:
        out["ip"] = data["ip"]
    if "domain" in data:
        out["domain"] = data["domain"]
    if "port" in data:
        out["port"] = data["port"]
    if "location" in data:
        import capo_guardduty.types.network_geo_location

        out["location"] = capo_guardduty.types.network_geo_location.deserialize_json(
            data["location"]
        )
    if "autonomousSystem" in data:
        import capo_guardduty.types.autonomous_system

        out["autonomous_system"] = (
            capo_guardduty.types.autonomous_system.deserialize_json(
                data["autonomousSystem"]
            )
        )
    if "connection" in data:
        import capo_guardduty.types.network_connection

        out["connection"] = capo_guardduty.types.network_connection.deserialize_json(
            data["connection"]
        )
    return out
