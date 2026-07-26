"""Generated from Smithy shape ``com.amazonaws.ecs#NetworkInterfaces``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.network_interface

NetworkInterfaces: TypeAlias = list["capo_ecs.types.network_interface.NetworkInterface"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkInterfaces) -> list:
    import capo_ecs.types.network_interface

    out: list = []
    for item in value:
        out.append(capo_ecs.types.network_interface.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> NetworkInterfaces:
    import capo_ecs.types.network_interface

    out: NetworkInterfaces = []
    for item in data:
        out.append(capo_ecs.types.network_interface.deserialize_aws_json_1_1(item))
    return out
