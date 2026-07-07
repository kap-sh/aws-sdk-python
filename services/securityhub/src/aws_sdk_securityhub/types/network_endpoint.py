"""Generated from Smithy shape ``com.amazonaws.securityhub#NetworkEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.network_autonomous_system
    import aws_sdk_securityhub.types.network_connection
    import aws_sdk_securityhub.types.network_geo_location
    import aws_sdk_securityhub.types.non_empty_string


class NetworkEndpoint(TypedDict, closed=True):
    id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The identifier of the network endpoint involved in the attack sequence. </p>"""
    ip: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The IP address used in the network endpoint. </p>"""
    domain: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The domain information for the network endpoint. </p>"""
    port: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p> The port number associated with the network endpoint. </p>"""
    location: NotRequired[
        "aws_sdk_securityhub.types.network_geo_location.NetworkGeoLocation"
    ]
    """<p> Information about the location of the network endpoint. </p>"""
    autonomous_system: NotRequired[
        "aws_sdk_securityhub.types.network_autonomous_system.NetworkAutonomousSystem"
    ]
    """<p> The Autonomous System Number (ASN) of the network endpoint. </p>"""
    connection: NotRequired[
        "aws_sdk_securityhub.types.network_connection.NetworkConnection"
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
        import aws_sdk_securityhub.types.network_geo_location

        out["Location"] = aws_sdk_securityhub.types.network_geo_location.serialize_json(
            value["location"]
        )
    if "autonomous_system" in value:
        import aws_sdk_securityhub.types.network_autonomous_system

        out["AutonomousSystem"] = (
            aws_sdk_securityhub.types.network_autonomous_system.serialize_json(
                value["autonomous_system"]
            )
        )
    if "connection" in value:
        import aws_sdk_securityhub.types.network_connection

        out["Connection"] = aws_sdk_securityhub.types.network_connection.serialize_json(
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
        import aws_sdk_securityhub.types.network_geo_location

        out["location"] = (
            aws_sdk_securityhub.types.network_geo_location.deserialize_json(
                data["Location"]
            )
        )
    if "AutonomousSystem" in data:
        import aws_sdk_securityhub.types.network_autonomous_system

        out["autonomous_system"] = (
            aws_sdk_securityhub.types.network_autonomous_system.deserialize_json(
                data["AutonomousSystem"]
            )
        )
    if "Connection" in data:
        import aws_sdk_securityhub.types.network_connection

        out["connection"] = (
            aws_sdk_securityhub.types.network_connection.deserialize_json(
                data["Connection"]
            )
        )
    return out
