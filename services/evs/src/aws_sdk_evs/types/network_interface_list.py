"""Generated from Smithy shape ``com.amazonaws.evs#NetworkInterfaceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_evs.types.network_interface

NetworkInterfaceList: TypeAlias = list[
    "aws_sdk_evs.types.network_interface.NetworkInterface"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NetworkInterfaceList) -> list:
    import aws_sdk_evs.types.network_interface

    out: list = []
    for item in value:
        out.append(aws_sdk_evs.types.network_interface.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> NetworkInterfaceList:
    import aws_sdk_evs.types.network_interface

    out: NetworkInterfaceList = []
    for item in data:
        out.append(aws_sdk_evs.types.network_interface.deserialize_aws_json_1_0(item))
    return out
