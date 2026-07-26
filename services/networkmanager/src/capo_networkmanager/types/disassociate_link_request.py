"""Generated from Smithy shape ``com.amazonaws.networkmanager#DisassociateLinkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.device_id
    import capo_networkmanager.types.global_network_id
    import capo_networkmanager.types.link_id


class DisassociateLinkRequest(TypedDict, closed=True):
    global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    device_id: "capo_networkmanager.types.device_id.DeviceId"
    """<p>The ID of the device.</p>"""
    link_id: "capo_networkmanager.types.link_id.LinkId"
    """<p>The ID of the link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateLinkRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateLinkRequest:
    out: DisassociateLinkRequest = {}  # type: ignore[typeddict-item]
    return out
