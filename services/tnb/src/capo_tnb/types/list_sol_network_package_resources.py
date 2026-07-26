"""Generated from Smithy shape ``com.amazonaws.tnb#ListSolNetworkPackageResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_tnb.types.list_sol_network_package_info

ListSolNetworkPackageResources: TypeAlias = list[
    "capo_tnb.types.list_sol_network_package_info.ListSolNetworkPackageInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListSolNetworkPackageResources) -> list:
    import capo_tnb.types.list_sol_network_package_info

    out: list = []
    for item in value:
        out.append(capo_tnb.types.list_sol_network_package_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListSolNetworkPackageResources:
    import capo_tnb.types.list_sol_network_package_info

    out: ListSolNetworkPackageResources = []
    for item in data:
        out.append(capo_tnb.types.list_sol_network_package_info.deserialize_json(item))
    return out
