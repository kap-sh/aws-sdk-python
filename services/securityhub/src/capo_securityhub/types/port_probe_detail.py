"""Generated from Smithy shape ``com.amazonaws.securityhub#PortProbeDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.action_local_ip_details
    import capo_securityhub.types.action_local_port_details
    import capo_securityhub.types.action_remote_ip_details


class PortProbeDetail(TypedDict, closed=True):
    local_port_details: NotRequired[
        "capo_securityhub.types.action_local_port_details.ActionLocalPortDetails"
    ]
    """<p>Provides information about the port that was scanned.</p>"""
    local_ip_details: NotRequired[
        "capo_securityhub.types.action_local_ip_details.ActionLocalIpDetails"
    ]
    """<p>Provides information about the IP address where the scanned port is located.</p>"""
    remote_ip_details: NotRequired[
        "capo_securityhub.types.action_remote_ip_details.ActionRemoteIpDetails"
    ]
    """<p>Provides information about the remote IP address that performed the scan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PortProbeDetail) -> dict:
    out: dict = {}
    if "local_port_details" in value:
        import capo_securityhub.types.action_local_port_details

        out["LocalPortDetails"] = (
            capo_securityhub.types.action_local_port_details.serialize_json(
                value["local_port_details"]
            )
        )
    if "local_ip_details" in value:
        import capo_securityhub.types.action_local_ip_details

        out["LocalIpDetails"] = (
            capo_securityhub.types.action_local_ip_details.serialize_json(
                value["local_ip_details"]
            )
        )
    if "remote_ip_details" in value:
        import capo_securityhub.types.action_remote_ip_details

        out["RemoteIpDetails"] = (
            capo_securityhub.types.action_remote_ip_details.serialize_json(
                value["remote_ip_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> PortProbeDetail:
    out: PortProbeDetail = {}  # type: ignore[typeddict-item]
    if "LocalPortDetails" in data:
        import capo_securityhub.types.action_local_port_details

        out["local_port_details"] = (
            capo_securityhub.types.action_local_port_details.deserialize_json(
                data["LocalPortDetails"]
            )
        )
    if "LocalIpDetails" in data:
        import capo_securityhub.types.action_local_ip_details

        out["local_ip_details"] = (
            capo_securityhub.types.action_local_ip_details.deserialize_json(
                data["LocalIpDetails"]
            )
        )
    if "RemoteIpDetails" in data:
        import capo_securityhub.types.action_remote_ip_details

        out["remote_ip_details"] = (
            capo_securityhub.types.action_remote_ip_details.deserialize_json(
                data["RemoteIpDetails"]
            )
        )
    return out
