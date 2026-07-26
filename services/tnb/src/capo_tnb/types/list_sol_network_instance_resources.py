"""Generated from Smithy shape ``com.amazonaws.tnb#ListSolNetworkInstanceResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_tnb.types.list_sol_network_instance_info

ListSolNetworkInstanceResources: TypeAlias = list[
    "capo_tnb.types.list_sol_network_instance_info.ListSolNetworkInstanceInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListSolNetworkInstanceResources) -> list:
    import capo_tnb.types.list_sol_network_instance_info

    out: list = []
    for item in value:
        out.append(capo_tnb.types.list_sol_network_instance_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListSolNetworkInstanceResources:
    import capo_tnb.types.list_sol_network_instance_info

    out: ListSolNetworkInstanceResources = []
    for item in data:
        out.append(capo_tnb.types.list_sol_network_instance_info.deserialize_json(item))
    return out
