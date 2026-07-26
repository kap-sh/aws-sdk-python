"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#NetworkInterfaces``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotfleetwise.types.network_interface

NetworkInterfaces: TypeAlias = list[
    "capo_iotfleetwise.types.network_interface.NetworkInterface"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NetworkInterfaces) -> list:
    import capo_iotfleetwise.types.network_interface

    out: list = []
    for item in value:
        out.append(
            capo_iotfleetwise.types.network_interface.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> NetworkInterfaces:
    import capo_iotfleetwise.types.network_interface

    out: NetworkInterfaces = []
    for item in data:
        out.append(
            capo_iotfleetwise.types.network_interface.deserialize_aws_json_1_0(item)
        )
    return out
