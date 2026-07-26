"""Generated from Smithy shape ``com.amazonaws.internetmonitor#NetworkList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_internetmonitor.types.network

NetworkList: TypeAlias = list["capo_internetmonitor.types.network.Network"]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkList) -> list:
    import capo_internetmonitor.types.network

    out: list = []
    for item in value:
        out.append(capo_internetmonitor.types.network.serialize_json(item))
    return out


def deserialize_json(data: list) -> NetworkList:
    import capo_internetmonitor.types.network

    out: NetworkList = []
    for item in data:
        out.append(capo_internetmonitor.types.network.deserialize_json(item))
    return out
