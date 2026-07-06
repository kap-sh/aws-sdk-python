"""Generated from Smithy shape ``com.amazonaws.networkmanager#ConnectPeerAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.connect_peer_association_state
    import aws_sdk_networkmanager.types.connect_peer_id
    import aws_sdk_networkmanager.types.device_id
    import aws_sdk_networkmanager.types.global_network_id
    import aws_sdk_networkmanager.types.link_id


class ConnectPeerAssociation(TypedDict, closed=True):
    connect_peer_id: NotRequired[
        "aws_sdk_networkmanager.types.connect_peer_id.ConnectPeerId"
    ]
    """<p>The ID of the Connect peer.</p>"""
    global_network_id: NotRequired[
        "aws_sdk_networkmanager.types.global_network_id.GlobalNetworkId"
    ]
    """<p>The ID of the global network.</p>"""
    device_id: NotRequired["aws_sdk_networkmanager.types.device_id.DeviceId"]
    """<p>The ID of the device to connect to.</p>"""
    link_id: NotRequired["aws_sdk_networkmanager.types.link_id.LinkId"]
    """<p>The ID of the link.</p>"""
    state: NotRequired[
        "aws_sdk_networkmanager.types.connect_peer_association_state.ConnectPeerAssociationState"
    ]
    """<p>The state of the Connect peer association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectPeerAssociation) -> dict:
    out: dict = {}
    if "connect_peer_id" in value:
        out["ConnectPeerId"] = value["connect_peer_id"]
    if "global_network_id" in value:
        out["GlobalNetworkId"] = value["global_network_id"]
    if "device_id" in value:
        out["DeviceId"] = value["device_id"]
    if "link_id" in value:
        out["LinkId"] = value["link_id"]
    if "state" in value:
        import aws_sdk_networkmanager.types.connect_peer_association_state

        out["State"] = (
            aws_sdk_networkmanager.types.connect_peer_association_state.serialize_json(
                value["state"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConnectPeerAssociation:
    out: ConnectPeerAssociation = {}  # type: ignore[typeddict-item]
    if "ConnectPeerId" in data:
        out["connect_peer_id"] = data["ConnectPeerId"]
    if "GlobalNetworkId" in data:
        out["global_network_id"] = data["GlobalNetworkId"]
    if "DeviceId" in data:
        out["device_id"] = data["DeviceId"]
    if "LinkId" in data:
        out["link_id"] = data["LinkId"]
    if "State" in data:
        import aws_sdk_networkmanager.types.connect_peer_association_state

        out["state"] = (
            aws_sdk_networkmanager.types.connect_peer_association_state.deserialize_json(
                data["State"]
            )
        )
    return out
