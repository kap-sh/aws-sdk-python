"""Generated from Smithy shape ``com.amazonaws.networkmanager#ConnectPeerIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.connect_peer_id

ConnectPeerIdList: TypeAlias = list[
    "capo_networkmanager.types.connect_peer_id.ConnectPeerId"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectPeerIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> ConnectPeerIdList:
    return list(data)
