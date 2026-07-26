"""Generated from Smithy shape ``com.amazonaws.tnb#ListSolNetworkOperationsResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_tnb.types.list_sol_network_operations_info

ListSolNetworkOperationsResources: TypeAlias = list[
    "capo_tnb.types.list_sol_network_operations_info.ListSolNetworkOperationsInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListSolNetworkOperationsResources) -> list:
    import capo_tnb.types.list_sol_network_operations_info

    out: list = []
    for item in value:
        out.append(capo_tnb.types.list_sol_network_operations_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListSolNetworkOperationsResources:
    import capo_tnb.types.list_sol_network_operations_info

    out: ListSolNetworkOperationsResources = []
    for item in data:
        out.append(
            capo_tnb.types.list_sol_network_operations_info.deserialize_json(item)
        )
    return out
