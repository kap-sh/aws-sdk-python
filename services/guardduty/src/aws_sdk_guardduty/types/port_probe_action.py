"""Generated from Smithy shape ``com.amazonaws.guardduty#PortProbeAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.boolean
    import aws_sdk_guardduty.types.port_probe_details


class PortProbeAction(TypedDict, closed=True):
    blocked: NotRequired["aws_sdk_guardduty.types.boolean.Boolean"]
    """<p>Indicates whether EC2 blocked the port probe to the instance, such as with an ACL.</p>"""
    port_probe_details: NotRequired[
        "aws_sdk_guardduty.types.port_probe_details.PortProbeDetails"
    ]
    """<p>A list of objects related to port probe details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PortProbeAction) -> dict:
    out: dict = {}
    if "blocked" in value:
        out["blocked"] = value["blocked"]
    if "port_probe_details" in value:
        import aws_sdk_guardduty.types.port_probe_details

        out["portProbeDetails"] = (
            aws_sdk_guardduty.types.port_probe_details.serialize_json(
                value["port_probe_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> PortProbeAction:
    out: PortProbeAction = {}  # type: ignore[typeddict-item]
    if "blocked" in data:
        out["blocked"] = data["blocked"]
    if "portProbeDetails" in data:
        import aws_sdk_guardduty.types.port_probe_details

        out["port_probe_details"] = (
            aws_sdk_guardduty.types.port_probe_details.deserialize_json(
                data["portProbeDetails"]
            )
        )
    return out
