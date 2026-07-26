"""Generated from Smithy shape ``com.amazonaws.networkmanager#LinkAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.device_id
    import capo_networkmanager.types.global_network_id
    import capo_networkmanager.types.link_association_state
    import capo_networkmanager.types.link_id


class LinkAssociation(TypedDict, closed=True):
    global_network_id: NotRequired[
        "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    ]
    """<p>The ID of the global network.</p>"""
    device_id: NotRequired["capo_networkmanager.types.device_id.DeviceId"]
    """<p>The device ID for the link association.</p>"""
    link_id: NotRequired["capo_networkmanager.types.link_id.LinkId"]
    """<p>The ID of the link.</p>"""
    link_association_state: NotRequired[
        "capo_networkmanager.types.link_association_state.LinkAssociationState"
    ]
    """<p>The state of the association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LinkAssociation) -> dict:
    out: dict = {}
    if "global_network_id" in value:
        out["GlobalNetworkId"] = value["global_network_id"]
    if "device_id" in value:
        out["DeviceId"] = value["device_id"]
    if "link_id" in value:
        out["LinkId"] = value["link_id"]
    if "link_association_state" in value:
        import capo_networkmanager.types.link_association_state

        out["LinkAssociationState"] = (
            capo_networkmanager.types.link_association_state.serialize_json(
                value["link_association_state"]
            )
        )
    return out


def deserialize_json(data: dict) -> LinkAssociation:
    out: LinkAssociation = {}  # type: ignore[typeddict-item]
    if "GlobalNetworkId" in data:
        out["global_network_id"] = data["GlobalNetworkId"]
    if "DeviceId" in data:
        out["device_id"] = data["DeviceId"]
    if "LinkId" in data:
        out["link_id"] = data["LinkId"]
    if "LinkAssociationState" in data:
        import capo_networkmanager.types.link_association_state

        out["link_association_state"] = (
            capo_networkmanager.types.link_association_state.deserialize_json(
                data["LinkAssociationState"]
            )
        )
    return out
