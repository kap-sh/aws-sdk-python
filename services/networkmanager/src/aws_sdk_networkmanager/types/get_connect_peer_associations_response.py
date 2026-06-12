"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetConnectPeerAssociationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.connect_peer_association_list
    import aws_sdk_networkmanager.types.next_token


class GetConnectPeerAssociationsResponse(TypedDict):
    connect_peer_associations: NotRequired[
        "aws_sdk_networkmanager.types.connect_peer_association_list.ConnectPeerAssociationList"
    ]
    """<p>Displays a list of Connect peer associations.</p>"""
    next_token: NotRequired["aws_sdk_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectPeerAssociationsResponse) -> dict:
    out: dict = {}
    if "connect_peer_associations" in value:
        import aws_sdk_networkmanager.types.connect_peer_association_list

        out["ConnectPeerAssociations"] = (
            aws_sdk_networkmanager.types.connect_peer_association_list.serialize_json(
                value["connect_peer_associations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetConnectPeerAssociationsResponse:
    out: GetConnectPeerAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "ConnectPeerAssociations" in data:
        import aws_sdk_networkmanager.types.connect_peer_association_list

        out["connect_peer_associations"] = (
            aws_sdk_networkmanager.types.connect_peer_association_list.deserialize_json(
                data["ConnectPeerAssociations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
