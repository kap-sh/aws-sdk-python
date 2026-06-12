"""Generated from Smithy shape ``com.amazonaws.networkmanager#DeleteConnectPeerRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.connect_peer_id


class DeleteConnectPeerRequest(TypedDict):
    connect_peer_id: "aws_sdk_networkmanager.types.connect_peer_id.ConnectPeerId"
    """<p>The ID of the deleted Connect peer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConnectPeerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConnectPeerRequest:
    out: DeleteConnectPeerRequest = {}  # type: ignore[typeddict-item]
    return out
