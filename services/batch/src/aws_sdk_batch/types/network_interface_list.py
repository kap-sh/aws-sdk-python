"""Generated from Smithy shape ``com.amazonaws.batch#NetworkInterfaceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.network_interface

NetworkInterfaceList: TypeAlias = list[
    "aws_sdk_batch.types.network_interface.NetworkInterface"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkInterfaceList) -> list:
    import aws_sdk_batch.types.network_interface

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.network_interface.serialize_json(item))
    return out


def deserialize_json(data: list) -> NetworkInterfaceList:
    import aws_sdk_batch.types.network_interface

    out: NetworkInterfaceList = []
    for item in data:
        out.append(aws_sdk_batch.types.network_interface.deserialize_json(item))
    return out
