"""Generated from Smithy shape ``com.amazonaws.networkmanager#Connection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.connection_arn
    import capo_networkmanager.types.connection_id
    import capo_networkmanager.types.connection_state
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.date_time
    import capo_networkmanager.types.device_id
    import capo_networkmanager.types.global_network_id
    import capo_networkmanager.types.link_id
    import capo_networkmanager.types.tag_list


class Connection(TypedDict, closed=True):
    connection_id: NotRequired["capo_networkmanager.types.connection_id.ConnectionId"]
    """<p>The ID of the connection.</p>"""
    connection_arn: NotRequired[
        "capo_networkmanager.types.connection_arn.ConnectionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the connection.</p>"""
    global_network_id: NotRequired[
        "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    ]
    """<p>The ID of the global network.</p>"""
    device_id: NotRequired["capo_networkmanager.types.device_id.DeviceId"]
    """<p>The ID of the first device in the connection.</p>"""
    connected_device_id: NotRequired["capo_networkmanager.types.device_id.DeviceId"]
    """<p>The ID of the second device in the connection.</p>"""
    link_id: NotRequired["capo_networkmanager.types.link_id.LinkId"]
    """<p>The ID of the link for the first device in the connection.</p>"""
    connected_link_id: NotRequired["capo_networkmanager.types.link_id.LinkId"]
    """<p>The ID of the link for the second device in the connection.</p>"""
    description: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The description of the connection.</p>"""
    created_at: NotRequired["capo_networkmanager.types.date_time.DateTime"]
    """<p>The date and time that the connection was created.</p>"""
    state: NotRequired["capo_networkmanager.types.connection_state.ConnectionState"]
    """<p>The state of the connection.</p>"""
    tags: NotRequired["capo_networkmanager.types.tag_list.TagList"]
    """<p>The tags for the connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Connection) -> dict:
    out: dict = {}
    if "connection_id" in value:
        out["ConnectionId"] = value["connection_id"]
    if "connection_arn" in value:
        out["ConnectionArn"] = value["connection_arn"]
    if "global_network_id" in value:
        out["GlobalNetworkId"] = value["global_network_id"]
    if "device_id" in value:
        out["DeviceId"] = value["device_id"]
    if "connected_device_id" in value:
        out["ConnectedDeviceId"] = value["connected_device_id"]
    if "link_id" in value:
        out["LinkId"] = value["link_id"]
    if "connected_link_id" in value:
        out["ConnectedLinkId"] = value["connected_link_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "created_at" in value:
        import capo_networkmanager.types.date_time

        out["CreatedAt"] = capo_networkmanager.types.date_time.serialize_json(
            value["created_at"]
        )
    if "state" in value:
        import capo_networkmanager.types.connection_state

        out["State"] = capo_networkmanager.types.connection_state.serialize_json(
            value["state"]
        )
    if "tags" in value:
        import capo_networkmanager.types.tag_list

        out["Tags"] = capo_networkmanager.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> Connection:
    out: Connection = {}  # type: ignore[typeddict-item]
    if "ConnectionId" in data:
        out["connection_id"] = data["ConnectionId"]
    if "ConnectionArn" in data:
        out["connection_arn"] = data["ConnectionArn"]
    if "GlobalNetworkId" in data:
        out["global_network_id"] = data["GlobalNetworkId"]
    if "DeviceId" in data:
        out["device_id"] = data["DeviceId"]
    if "ConnectedDeviceId" in data:
        out["connected_device_id"] = data["ConnectedDeviceId"]
    if "LinkId" in data:
        out["link_id"] = data["LinkId"]
    if "ConnectedLinkId" in data:
        out["connected_link_id"] = data["ConnectedLinkId"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreatedAt" in data:
        import capo_networkmanager.types.date_time

        out["created_at"] = capo_networkmanager.types.date_time.deserialize_json(
            data["CreatedAt"]
        )
    if "State" in data:
        import capo_networkmanager.types.connection_state

        out["state"] = capo_networkmanager.types.connection_state.deserialize_json(
            data["State"]
        )
    if "Tags" in data:
        import capo_networkmanager.types.tag_list

        out["tags"] = capo_networkmanager.types.tag_list.deserialize_json(data["Tags"])
    return out
