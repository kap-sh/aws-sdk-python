"""Generated from Smithy shape ``com.amazonaws.networkmanager#ListConnectPeersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.connect_peer_summary_list
    import aws_sdk_networkmanager.types.next_token


class ListConnectPeersResponse(TypedDict):
    connect_peers: NotRequired[
        "aws_sdk_networkmanager.types.connect_peer_summary_list.ConnectPeerSummaryList"
    ]
    """<p>Describes the Connect peers.</p>"""
    next_token: NotRequired["aws_sdk_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConnectPeersResponse) -> dict:
    out: dict = {}
    if "connect_peers" in value:
        import aws_sdk_networkmanager.types.connect_peer_summary_list

        out["ConnectPeers"] = (
            aws_sdk_networkmanager.types.connect_peer_summary_list.serialize_json(
                value["connect_peers"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConnectPeersResponse:
    out: ListConnectPeersResponse = {}  # type: ignore[typeddict-item]
    if "ConnectPeers" in data:
        import aws_sdk_networkmanager.types.connect_peer_summary_list

        out["connect_peers"] = (
            aws_sdk_networkmanager.types.connect_peer_summary_list.deserialize_json(
                data["ConnectPeers"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
