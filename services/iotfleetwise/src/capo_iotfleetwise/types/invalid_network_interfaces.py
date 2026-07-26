"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#InvalidNetworkInterfaces``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotfleetwise.types.invalid_network_interface

InvalidNetworkInterfaces: TypeAlias = list[
    "capo_iotfleetwise.types.invalid_network_interface.InvalidNetworkInterface"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvalidNetworkInterfaces) -> list:
    import capo_iotfleetwise.types.invalid_network_interface

    out: list = []
    for item in value:
        out.append(
            capo_iotfleetwise.types.invalid_network_interface.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> InvalidNetworkInterfaces:
    import capo_iotfleetwise.types.invalid_network_interface

    out: InvalidNetworkInterfaces = []
    for item in data:
        out.append(
            capo_iotfleetwise.types.invalid_network_interface.deserialize_aws_json_1_0(
                item
            )
        )
    return out
