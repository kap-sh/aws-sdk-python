"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetConnectPeerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.connect_peer_id


class GetConnectPeerRequest(TypedDict, closed=True):
    connect_peer_id: "aws_sdk_networkmanager.types.connect_peer_id.ConnectPeerId"
    """<p>The ID of the Connect peer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectPeerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetConnectPeerRequest:
    out: GetConnectPeerRequest = {}  # type: ignore[typeddict-item]
    return out
