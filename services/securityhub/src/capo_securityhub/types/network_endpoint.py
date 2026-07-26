"""Generated from Smithy shape ``com.amazonaws.securityhub#NetworkEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.integer
    import capo_securityhub.types.network_autonomous_system
    import capo_securityhub.types.network_connection
    import capo_securityhub.types.network_geo_location
    import capo_securityhub.types.non_empty_string


class NetworkEndpoint(TypedDict, closed=True):
    id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The identifier of the network endpoint involved in the attack sequence. </p>"""
    ip: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The IP address used in the network endpoint. </p>"""
    domain: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The domain information for the network endpoint. </p>"""
    port: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p> The port number associated with the network endpoint. </p>"""
    location: NotRequired[
        "capo_securityhub.types.network_geo_location.NetworkGeoLocation"
    ]
    """<p> Information about the location of the network endpoint. </p>"""
    autonomous_system: NotRequired[
        "capo_securityhub.types.network_autonomous_system.NetworkAutonomousSystem"
    ]
    """<p> The Autonomous System Number (ASN) of the network endpoint. </p>"""
    connection: NotRequired[
        "capo_securityhub.types.network_connection.NetworkConnection"
    ]
    """<p> Information about the network connection. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkEndpoint) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "ip" in value:
        out["Ip"] = value["ip"]
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "port" in value:
        out["Port"] = value["port"]
    if "location" in value:
        import capo_securityhub.types.network_geo_location

        out["Location"] = capo_securityhub.types.network_geo_location.serialize_json(
            value["location"]
        )
    if "autonomous_system" in value:
        import capo_securityhub.types.network_autonomous_system

        out["AutonomousSystem"] = (
            capo_securityhub.types.network_autonomous_system.serialize_json(
                value["autonomous_system"]
            )
        )
    if "connection" in value:
        import capo_securityhub.types.network_connection

        out["Connection"] = capo_securityhub.types.network_connection.serialize_json(
            value["connection"]
        )
    return out


def deserialize_json(data: dict) -> NetworkEndpoint:
    out: NetworkEndpoint = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Ip" in data:
        out["ip"] = data["Ip"]
    if "Domain" in data:
        out["domain"] = data["Domain"]
    if "Port" in data:
        out["port"] = data["Port"]
    if "Location" in data:
        import capo_securityhub.types.network_geo_location

        out["location"] = capo_securityhub.types.network_geo_location.deserialize_json(
            data["Location"]
        )
    if "AutonomousSystem" in data:
        import capo_securityhub.types.network_autonomous_system

        out["autonomous_system"] = (
            capo_securityhub.types.network_autonomous_system.deserialize_json(
                data["AutonomousSystem"]
            )
        )
    if "Connection" in data:
        import capo_securityhub.types.network_connection

        out["connection"] = capo_securityhub.types.network_connection.deserialize_json(
            data["Connection"]
        )
    return out
