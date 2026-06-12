"""Generated from Smithy shape ``com.amazonaws.networkmanager#UpdateConnectionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.connection_id
    import aws_sdk_networkmanager.types.constrained_string
    import aws_sdk_networkmanager.types.global_network_id
    import aws_sdk_networkmanager.types.link_id


class UpdateConnectionRequest(TypedDict):
    global_network_id: "aws_sdk_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    connection_id: "aws_sdk_networkmanager.types.connection_id.ConnectionId"
    """<p>The ID of the connection.</p>"""
    link_id: NotRequired["aws_sdk_networkmanager.types.link_id.LinkId"]
    """<p>The ID of the link for the first device in the connection.</p>"""
    connected_link_id: NotRequired["aws_sdk_networkmanager.types.link_id.LinkId"]
    """<p>The ID of the link for the second device in the connection.</p>"""
    description: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>A description of the connection.</p> <p>Length Constraints: Maximum length of 256 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConnectionRequest) -> dict:
    out: dict = {}
    if "link_id" in value:
        out["LinkId"] = value["link_id"]
    if "connected_link_id" in value:
        out["ConnectedLinkId"] = value["connected_link_id"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateConnectionRequest:
    out: UpdateConnectionRequest = {}  # type: ignore[typeddict-item]
    if "LinkId" in data:
        out["link_id"] = data["LinkId"]
    if "ConnectedLinkId" in data:
        out["connected_link_id"] = data["ConnectedLinkId"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
