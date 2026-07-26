"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#SocketAddresses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_global_accelerator.types.socket_address

SocketAddresses: TypeAlias = list[
    "capo_global_accelerator.types.socket_address.SocketAddress"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SocketAddresses) -> list:
    import capo_global_accelerator.types.socket_address

    out: list = []
    for item in value:
        out.append(
            capo_global_accelerator.types.socket_address.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SocketAddresses:
    import capo_global_accelerator.types.socket_address

    out: SocketAddresses = []
    for item in data:
        out.append(
            capo_global_accelerator.types.socket_address.deserialize_aws_json_1_1(item)
        )
    return out
