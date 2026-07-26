"""Generated from Smithy shape ``com.amazonaws.drs#SourceNetworksList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_drs.types.source_network

SourceNetworksList: TypeAlias = list["capo_drs.types.source_network.SourceNetwork"]


# --- restJson1 ser/de ---
def serialize_json(value: SourceNetworksList) -> list:
    import capo_drs.types.source_network

    out: list = []
    for item in value:
        out.append(capo_drs.types.source_network.serialize_json(item))
    return out


def deserialize_json(data: list) -> SourceNetworksList:
    import capo_drs.types.source_network

    out: SourceNetworksList = []
    for item in data:
        out.append(capo_drs.types.source_network.deserialize_json(item))
    return out
