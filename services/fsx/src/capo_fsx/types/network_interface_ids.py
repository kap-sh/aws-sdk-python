"""Generated from Smithy shape ``com.amazonaws.fsx#NetworkInterfaceIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fsx.types.network_interface_id

NetworkInterfaceIds: TypeAlias = list[
    "capo_fsx.types.network_interface_id.NetworkInterfaceId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkInterfaceIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> NetworkInterfaceIds:
    return list(data)
