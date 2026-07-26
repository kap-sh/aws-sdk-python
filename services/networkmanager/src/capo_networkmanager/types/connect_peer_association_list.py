"""Generated from Smithy shape ``com.amazonaws.networkmanager#ConnectPeerAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.connect_peer_association

ConnectPeerAssociationList: TypeAlias = list[
    "capo_networkmanager.types.connect_peer_association.ConnectPeerAssociation"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectPeerAssociationList) -> list:
    import capo_networkmanager.types.connect_peer_association

    out: list = []
    for item in value:
        out.append(
            capo_networkmanager.types.connect_peer_association.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ConnectPeerAssociationList:
    import capo_networkmanager.types.connect_peer_association

    out: ConnectPeerAssociationList = []
    for item in data:
        out.append(
            capo_networkmanager.types.connect_peer_association.deserialize_json(item)
        )
    return out
