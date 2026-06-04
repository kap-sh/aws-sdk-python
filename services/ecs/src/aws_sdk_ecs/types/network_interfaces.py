"""Generated from Smithy shape ``com.amazonaws.ecs#NetworkInterfaces``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.network_interface

NetworkInterfaces: TypeAlias = list[
    "aws_sdk_ecs.types.network_interface.NetworkInterface"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkInterfaces) -> list:
    import aws_sdk_ecs.types.network_interface

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.network_interface.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> NetworkInterfaces:
    import aws_sdk_ecs.types.network_interface

    out: NetworkInterfaces = []
    for item in data:
        out.append(aws_sdk_ecs.types.network_interface.deserialize_aws_json_1_1(item))
    return out
