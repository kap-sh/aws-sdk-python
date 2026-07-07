"""Generated from Smithy shape ``com.amazonaws.guardduty#PortProbeDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.local_ip_details
    import aws_sdk_guardduty.types.local_port_details
    import aws_sdk_guardduty.types.remote_ip_details


class PortProbeDetail(TypedDict, closed=True):
    local_port_details: NotRequired[
        "aws_sdk_guardduty.types.local_port_details.LocalPortDetails"
    ]
    """<p>The local port information of the connection.</p>"""
    local_ip_details: NotRequired[
        "aws_sdk_guardduty.types.local_ip_details.LocalIpDetails"
    ]
    """<p>The local IP information of the connection.</p>"""
    remote_ip_details: NotRequired[
        "aws_sdk_guardduty.types.remote_ip_details.RemoteIpDetails"
    ]
    """<p>The remote IP information of the connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PortProbeDetail) -> dict:
    out: dict = {}
    if "local_port_details" in value:
        import aws_sdk_guardduty.types.local_port_details

        out["localPortDetails"] = (
            aws_sdk_guardduty.types.local_port_details.serialize_json(
                value["local_port_details"]
            )
        )
    if "local_ip_details" in value:
        import aws_sdk_guardduty.types.local_ip_details

        out["localIpDetails"] = aws_sdk_guardduty.types.local_ip_details.serialize_json(
            value["local_ip_details"]
        )
    if "remote_ip_details" in value:
        import aws_sdk_guardduty.types.remote_ip_details

        out["remoteIpDetails"] = (
            aws_sdk_guardduty.types.remote_ip_details.serialize_json(
                value["remote_ip_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> PortProbeDetail:
    out: PortProbeDetail = {}  # type: ignore[typeddict-item]
    if "localPortDetails" in data:
        import aws_sdk_guardduty.types.local_port_details

        out["local_port_details"] = (
            aws_sdk_guardduty.types.local_port_details.deserialize_json(
                data["localPortDetails"]
            )
        )
    if "localIpDetails" in data:
        import aws_sdk_guardduty.types.local_ip_details

        out["local_ip_details"] = (
            aws_sdk_guardduty.types.local_ip_details.deserialize_json(
                data["localIpDetails"]
            )
        )
    if "remoteIpDetails" in data:
        import aws_sdk_guardduty.types.remote_ip_details

        out["remote_ip_details"] = (
            aws_sdk_guardduty.types.remote_ip_details.deserialize_json(
                data["remoteIpDetails"]
            )
        )
    return out
