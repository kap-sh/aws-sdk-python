"""Generated from Smithy shape ``com.amazonaws.inspector2#NetworkReachabilityDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.network_path
    import aws_sdk_inspector2.types.network_protocol
    import aws_sdk_inspector2.types.port_range


class NetworkReachabilityDetails(TypedDict, closed=True):
    open_port_range: "aws_sdk_inspector2.types.port_range.PortRange"
    """<p>An object that contains details about the open port range associated with a finding.</p>"""
    protocol: "aws_sdk_inspector2.types.network_protocol.NetworkProtocol"
    """<p>The protocol associated with a finding.</p>"""
    network_path: "aws_sdk_inspector2.types.network_path.NetworkPath"
    """<p>An object that contains details about a network path associated with a finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkReachabilityDetails) -> dict:
    out: dict = {}
    import aws_sdk_inspector2.types.port_range

    out["openPortRange"] = aws_sdk_inspector2.types.port_range.serialize_json(
        value["open_port_range"]
    )
    out["protocol"] = value["protocol"]
    import aws_sdk_inspector2.types.network_path

    out["networkPath"] = aws_sdk_inspector2.types.network_path.serialize_json(
        value["network_path"]
    )
    return out


def deserialize_json(data: dict) -> NetworkReachabilityDetails:
    out: NetworkReachabilityDetails = {}  # type: ignore[typeddict-item]
    if "openPortRange" in data:
        import aws_sdk_inspector2.types.port_range

        out["open_port_range"] = aws_sdk_inspector2.types.port_range.deserialize_json(
            data["openPortRange"]
        )
    else:
        raise DeserializationError(
            "NetworkReachabilityDetails.open_port_range required"
        )
    if "protocol" in data:
        out["protocol"] = data["protocol"]
    else:
        raise DeserializationError("NetworkReachabilityDetails.protocol required")
    if "networkPath" in data:
        import aws_sdk_inspector2.types.network_path

        out["network_path"] = aws_sdk_inspector2.types.network_path.deserialize_json(
            data["networkPath"]
        )
    else:
        raise DeserializationError("NetworkReachabilityDetails.network_path required")
    return out
