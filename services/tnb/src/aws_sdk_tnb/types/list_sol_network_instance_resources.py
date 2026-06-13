"""Generated from Smithy shape ``com.amazonaws.tnb#ListSolNetworkInstanceResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_tnb.types.list_sol_network_instance_info

ListSolNetworkInstanceResources: TypeAlias = list[
    "aws_sdk_tnb.types.list_sol_network_instance_info.ListSolNetworkInstanceInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListSolNetworkInstanceResources) -> list:
    import aws_sdk_tnb.types.list_sol_network_instance_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_tnb.types.list_sol_network_instance_info.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListSolNetworkInstanceResources:
    import aws_sdk_tnb.types.list_sol_network_instance_info

    out: ListSolNetworkInstanceResources = []
    for item in data:
        out.append(
            aws_sdk_tnb.types.list_sol_network_instance_info.deserialize_json(item)
        )
    return out
