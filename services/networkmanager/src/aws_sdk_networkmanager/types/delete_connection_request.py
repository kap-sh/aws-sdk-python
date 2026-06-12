"""Generated from Smithy shape ``com.amazonaws.networkmanager#DeleteConnectionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.connection_id
    import aws_sdk_networkmanager.types.global_network_id


class DeleteConnectionRequest(TypedDict):
    global_network_id: "aws_sdk_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    connection_id: "aws_sdk_networkmanager.types.connection_id.ConnectionId"
    """<p>The ID of the connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConnectionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConnectionRequest:
    out: DeleteConnectionRequest = {}  # type: ignore[typeddict-item]
    return out
