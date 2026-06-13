"""Generated from Smithy shape ``com.amazonaws.tnb#ListSolNetworkOperationsResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_tnb.types.list_sol_network_operations_info

ListSolNetworkOperationsResources: TypeAlias = list[
    "aws_sdk_tnb.types.list_sol_network_operations_info.ListSolNetworkOperationsInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListSolNetworkOperationsResources) -> list:
    import aws_sdk_tnb.types.list_sol_network_operations_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_tnb.types.list_sol_network_operations_info.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListSolNetworkOperationsResources:
    import aws_sdk_tnb.types.list_sol_network_operations_info

    out: ListSolNetworkOperationsResources = []
    for item in data:
        out.append(
            aws_sdk_tnb.types.list_sol_network_operations_info.deserialize_json(item)
        )
    return out
