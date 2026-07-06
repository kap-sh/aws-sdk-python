"""Generated from Smithy shape ``com.amazonaws.securityhub#NetworkConnectionAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.action_local_port_details
    import aws_sdk_securityhub.types.action_remote_ip_details
    import aws_sdk_securityhub.types.action_remote_port_details
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string


class NetworkConnectionAction(TypedDict, closed=True):
    connection_direction: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The direction of the network connection request (<code>IN</code> or <code>OUT</code>).</p>"""
    remote_ip_details: NotRequired[
        "aws_sdk_securityhub.types.action_remote_ip_details.ActionRemoteIpDetails"
    ]
    """<p>Information about the remote IP address that issued the network connection request.</p>"""
    remote_port_details: NotRequired[
        "aws_sdk_securityhub.types.action_remote_port_details.ActionRemotePortDetails"
    ]
    """<p>Information about the port on the remote IP address.</p>"""
    local_port_details: NotRequired[
        "aws_sdk_securityhub.types.action_local_port_details.ActionLocalPortDetails"
    ]
    """<p>Information about the port on the EC2 instance.</p>"""
    protocol: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The protocol used to make the network connection request.</p> <p>Length Constraints: Minimum length of 1. Maximum length of 64.</p>"""
    blocked: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether the network connection attempt was blocked.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkConnectionAction) -> dict:
    out: dict = {}
    if "connection_direction" in value:
        out["ConnectionDirection"] = value["connection_direction"]
    if "remote_ip_details" in value:
        import aws_sdk_securityhub.types.action_remote_ip_details

        out["RemoteIpDetails"] = (
            aws_sdk_securityhub.types.action_remote_ip_details.serialize_json(
                value["remote_ip_details"]
            )
        )
    if "remote_port_details" in value:
        import aws_sdk_securityhub.types.action_remote_port_details

        out["RemotePortDetails"] = (
            aws_sdk_securityhub.types.action_remote_port_details.serialize_json(
                value["remote_port_details"]
            )
        )
    if "local_port_details" in value:
        import aws_sdk_securityhub.types.action_local_port_details

        out["LocalPortDetails"] = (
            aws_sdk_securityhub.types.action_local_port_details.serialize_json(
                value["local_port_details"]
            )
        )
    if "protocol" in value:
        out["Protocol"] = value["protocol"]
    if "blocked" in value:
        out["Blocked"] = value["blocked"]
    return out


def deserialize_json(data: dict) -> NetworkConnectionAction:
    out: NetworkConnectionAction = {}  # type: ignore[typeddict-item]
    if "ConnectionDirection" in data:
        out["connection_direction"] = data["ConnectionDirection"]
    if "RemoteIpDetails" in data:
        import aws_sdk_securityhub.types.action_remote_ip_details

        out["remote_ip_details"] = (
            aws_sdk_securityhub.types.action_remote_ip_details.deserialize_json(
                data["RemoteIpDetails"]
            )
        )
    if "RemotePortDetails" in data:
        import aws_sdk_securityhub.types.action_remote_port_details

        out["remote_port_details"] = (
            aws_sdk_securityhub.types.action_remote_port_details.deserialize_json(
                data["RemotePortDetails"]
            )
        )
    if "LocalPortDetails" in data:
        import aws_sdk_securityhub.types.action_local_port_details

        out["local_port_details"] = (
            aws_sdk_securityhub.types.action_local_port_details.deserialize_json(
                data["LocalPortDetails"]
            )
        )
    if "Protocol" in data:
        out["protocol"] = data["Protocol"]
    if "Blocked" in data:
        out["blocked"] = data["Blocked"]
    return out
