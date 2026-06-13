"""Generated from Smithy shape ``com.amazonaws.tnb#ListSolNetworkPackageResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_tnb.types.list_sol_network_package_info

ListSolNetworkPackageResources: TypeAlias = list[
    "aws_sdk_tnb.types.list_sol_network_package_info.ListSolNetworkPackageInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListSolNetworkPackageResources) -> list:
    import aws_sdk_tnb.types.list_sol_network_package_info

    out: list = []
    for item in value:
        out.append(aws_sdk_tnb.types.list_sol_network_package_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListSolNetworkPackageResources:
    import aws_sdk_tnb.types.list_sol_network_package_info

    out: ListSolNetworkPackageResources = []
    for item in data:
        out.append(
            aws_sdk_tnb.types.list_sol_network_package_info.deserialize_json(item)
        )
    return out
