"""Generated from Smithy shape ``com.amazonaws.networkmanager#EdgeSetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.edge_set

EdgeSetList: TypeAlias = list["capo_networkmanager.types.edge_set.EdgeSet"]


# --- restJson1 ser/de ---
def serialize_json(value: EdgeSetList) -> list:
    import capo_networkmanager.types.edge_set

    out: list = []
    for item in value:
        out.append(capo_networkmanager.types.edge_set.serialize_json(item))
    return out


def deserialize_json(data: list) -> EdgeSetList:
    import capo_networkmanager.types.edge_set

    out: EdgeSetList = []
    for item in data:
        out.append(capo_networkmanager.types.edge_set.deserialize_json(item))
    return out
