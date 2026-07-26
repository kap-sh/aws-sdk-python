"""Generated from Smithy shape ``com.amazonaws.networkmanager#ConnectPeerErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.connect_peer_error

ConnectPeerErrorList: TypeAlias = list[
    "capo_networkmanager.types.connect_peer_error.ConnectPeerError"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectPeerErrorList) -> list:
    import capo_networkmanager.types.connect_peer_error

    out: list = []
    for item in value:
        out.append(capo_networkmanager.types.connect_peer_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConnectPeerErrorList:
    import capo_networkmanager.types.connect_peer_error

    out: ConnectPeerErrorList = []
    for item in data:
        out.append(capo_networkmanager.types.connect_peer_error.deserialize_json(item))
    return out
