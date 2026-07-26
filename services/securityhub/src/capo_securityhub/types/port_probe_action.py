"""Generated from Smithy shape ``com.amazonaws.securityhub#PortProbeAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.port_probe_detail_list


class PortProbeAction(TypedDict, closed=True):
    port_probe_details: NotRequired[
        "capo_securityhub.types.port_probe_detail_list.PortProbeDetailList"
    ]
    """<p>Information about the ports affected by the port probe.</p>"""
    blocked: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether the port probe was blocked.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PortProbeAction) -> dict:
    out: dict = {}
    if "port_probe_details" in value:
        import capo_securityhub.types.port_probe_detail_list

        out["PortProbeDetails"] = (
            capo_securityhub.types.port_probe_detail_list.serialize_json(
                value["port_probe_details"]
            )
        )
    if "blocked" in value:
        out["Blocked"] = value["blocked"]
    return out


def deserialize_json(data: dict) -> PortProbeAction:
    out: PortProbeAction = {}  # type: ignore[typeddict-item]
    if "PortProbeDetails" in data:
        import capo_securityhub.types.port_probe_detail_list

        out["port_probe_details"] = (
            capo_securityhub.types.port_probe_detail_list.deserialize_json(
                data["PortProbeDetails"]
            )
        )
    if "Blocked" in data:
        out["blocked"] = data["Blocked"]
    return out
