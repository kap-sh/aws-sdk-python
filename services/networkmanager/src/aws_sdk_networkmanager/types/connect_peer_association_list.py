"""Generated from Smithy shape ``com.amazonaws.networkmanager#ConnectPeerAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.connect_peer_association

ConnectPeerAssociationList: TypeAlias = list[
    "aws_sdk_networkmanager.types.connect_peer_association.ConnectPeerAssociation"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectPeerAssociationList) -> list:
    import aws_sdk_networkmanager.types.connect_peer_association

    out: list = []
    for item in value:
        out.append(
            aws_sdk_networkmanager.types.connect_peer_association.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ConnectPeerAssociationList:
    import aws_sdk_networkmanager.types.connect_peer_association

    out: ConnectPeerAssociationList = []
    for item in data:
        out.append(
            aws_sdk_networkmanager.types.connect_peer_association.deserialize_json(item)
        )
    return out
