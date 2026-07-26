"""Generated from Smithy shape ``com.amazonaws.wickr#NetworkList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wickr.types.network

NetworkList: TypeAlias = list["capo_wickr.types.network.Network"]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkList) -> list:
    import capo_wickr.types.network

    out: list = []
    for item in value:
        out.append(capo_wickr.types.network.serialize_json(item))
    return out


def deserialize_json(data: list) -> NetworkList:
    import capo_wickr.types.network

    out: NetworkList = []
    for item in data:
        out.append(capo_wickr.types.network.deserialize_json(item))
    return out
