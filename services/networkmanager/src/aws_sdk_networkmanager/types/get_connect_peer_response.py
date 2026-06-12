"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetConnectPeerResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.connect_peer


class GetConnectPeerResponse(TypedDict):
    connect_peer: NotRequired["aws_sdk_networkmanager.types.connect_peer.ConnectPeer"]
    """<p>Returns information about a core network Connect peer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectPeerResponse) -> dict:
    out: dict = {}
    if "connect_peer" in value:
        import aws_sdk_networkmanager.types.connect_peer

        out["ConnectPeer"] = aws_sdk_networkmanager.types.connect_peer.serialize_json(
            value["connect_peer"]
        )
    return out


def deserialize_json(data: dict) -> GetConnectPeerResponse:
    out: GetConnectPeerResponse = {}  # type: ignore[typeddict-item]
    if "ConnectPeer" in data:
        import aws_sdk_networkmanager.types.connect_peer

        out["connect_peer"] = (
            aws_sdk_networkmanager.types.connect_peer.deserialize_json(
                data["ConnectPeer"]
            )
        )
    return out
