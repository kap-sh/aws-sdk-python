"""Generated from Smithy shape ``com.amazonaws.mediaconnect#BatchGetRouterNetworkInterfaceErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.batch_get_router_network_interface_error

BatchGetRouterNetworkInterfaceErrorList: TypeAlias = list[
    "aws_sdk_mediaconnect.types.batch_get_router_network_interface_error.BatchGetRouterNetworkInterfaceError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetRouterNetworkInterfaceErrorList) -> list:
    import aws_sdk_mediaconnect.types.batch_get_router_network_interface_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mediaconnect.types.batch_get_router_network_interface_error.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchGetRouterNetworkInterfaceErrorList:
    import aws_sdk_mediaconnect.types.batch_get_router_network_interface_error

    out: BatchGetRouterNetworkInterfaceErrorList = []
    for item in data:
        out.append(
            aws_sdk_mediaconnect.types.batch_get_router_network_interface_error.deserialize_json(
                item
            )
        )
    return out
