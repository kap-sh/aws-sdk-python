"""Generated from Smithy shape ``com.amazonaws.mediaconnect#BatchGetRouterNetworkInterfaceErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.batch_get_router_network_interface_error

BatchGetRouterNetworkInterfaceErrorList: TypeAlias = list[
    "capo_mediaconnect.types.batch_get_router_network_interface_error.BatchGetRouterNetworkInterfaceError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetRouterNetworkInterfaceErrorList) -> list:
    import capo_mediaconnect.types.batch_get_router_network_interface_error

    out: list = []
    for item in value:
        out.append(
            capo_mediaconnect.types.batch_get_router_network_interface_error.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchGetRouterNetworkInterfaceErrorList:
    import capo_mediaconnect.types.batch_get_router_network_interface_error

    out: BatchGetRouterNetworkInterfaceErrorList = []
    for item in data:
        out.append(
            capo_mediaconnect.types.batch_get_router_network_interface_error.deserialize_json(
                item
            )
        )
    return out
