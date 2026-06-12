"""Generated from Smithy shape ``com.amazonaws.networkmanager#LinkAssociation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.device_id
    import aws_sdk_networkmanager.types.global_network_id
    import aws_sdk_networkmanager.types.link_association_state
    import aws_sdk_networkmanager.types.link_id


class LinkAssociation(TypedDict):
    global_network_id: NotRequired[
        "aws_sdk_networkmanager.types.global_network_id.GlobalNetworkId"
    ]
    """<p>The ID of the global network.</p>"""
    device_id: NotRequired["aws_sdk_networkmanager.types.device_id.DeviceId"]
    """<p>The device ID for the link association.</p>"""
    link_id: NotRequired["aws_sdk_networkmanager.types.link_id.LinkId"]
    """<p>The ID of the link.</p>"""
    link_association_state: NotRequired[
        "aws_sdk_networkmanager.types.link_association_state.LinkAssociationState"
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
        import aws_sdk_networkmanager.types.link_association_state

        out["LinkAssociationState"] = (
            aws_sdk_networkmanager.types.link_association_state.serialize_json(
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
        import aws_sdk_networkmanager.types.link_association_state

        out["link_association_state"] = (
            aws_sdk_networkmanager.types.link_association_state.deserialize_json(
                data["LinkAssociationState"]
            )
        )
    return out
