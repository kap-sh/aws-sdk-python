"""Generated from Smithy shape ``com.amazonaws.networkmanager#CreateConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_networkmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.device_id
    import capo_networkmanager.types.global_network_id
    import capo_networkmanager.types.link_id
    import capo_networkmanager.types.tag_list


class CreateConnectionRequest(TypedDict, closed=True):
    global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    device_id: "capo_networkmanager.types.device_id.DeviceId"
    """<p>The ID of the first device in the connection.</p>"""
    connected_device_id: "capo_networkmanager.types.device_id.DeviceId"
    """<p>The ID of the second device in the connection.</p>"""
    link_id: NotRequired["capo_networkmanager.types.link_id.LinkId"]
    """<p>The ID of the link for the first device.</p>"""
    connected_link_id: NotRequired["capo_networkmanager.types.link_id.LinkId"]
    """<p>The ID of the link for the second device.</p>"""
    description: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>A description of the connection.</p> <p>Length Constraints: Maximum length of 256 characters.</p>"""
    tags: NotRequired["capo_networkmanager.types.tag_list.TagList"]
    """<p>The tags to apply to the resource during creation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConnectionRequest) -> dict:
    out: dict = {}
    out["DeviceId"] = value["device_id"]
    out["ConnectedDeviceId"] = value["connected_device_id"]
    if "link_id" in value:
        out["LinkId"] = value["link_id"]
    if "connected_link_id" in value:
        out["ConnectedLinkId"] = value["connected_link_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_networkmanager.types.tag_list

        out["Tags"] = capo_networkmanager.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateConnectionRequest:
    out: CreateConnectionRequest = {}  # type: ignore[typeddict-item]
    if "DeviceId" in data:
        out["device_id"] = data["DeviceId"]
    else:
        raise DeserializationError("CreateConnectionRequest.device_id required")
    if "ConnectedDeviceId" in data:
        out["connected_device_id"] = data["ConnectedDeviceId"]
    else:
        raise DeserializationError(
            "CreateConnectionRequest.connected_device_id required"
        )
    if "LinkId" in data:
        out["link_id"] = data["LinkId"]
    if "ConnectedLinkId" in data:
        out["connected_link_id"] = data["ConnectedLinkId"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Tags" in data:
        import capo_networkmanager.types.tag_list

        out["tags"] = capo_networkmanager.types.tag_list.deserialize_json(data["Tags"])
    return out
