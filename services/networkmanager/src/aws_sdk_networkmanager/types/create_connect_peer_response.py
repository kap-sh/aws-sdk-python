"""Generated from Smithy shape ``com.amazonaws.networkmanager#CreateConnectPeerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.connect_peer


class CreateConnectPeerResponse(TypedDict, closed=True):
    connect_peer: NotRequired["aws_sdk_networkmanager.types.connect_peer.ConnectPeer"]
    """<p>The response to the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConnectPeerResponse) -> dict:
    out: dict = {}
    if "connect_peer" in value:
        import aws_sdk_networkmanager.types.connect_peer

        out["ConnectPeer"] = aws_sdk_networkmanager.types.connect_peer.serialize_json(
            value["connect_peer"]
        )
    return out


def deserialize_json(data: dict) -> CreateConnectPeerResponse:
    out: CreateConnectPeerResponse = {}  # type: ignore[typeddict-item]
    if "ConnectPeer" in data:
        import aws_sdk_networkmanager.types.connect_peer

        out["connect_peer"] = (
            aws_sdk_networkmanager.types.connect_peer.deserialize_json(
                data["ConnectPeer"]
            )
        )
    return out
