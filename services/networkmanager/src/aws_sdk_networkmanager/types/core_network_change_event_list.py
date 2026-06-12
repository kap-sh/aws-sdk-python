"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkChangeEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.core_network_change_event

CoreNetworkChangeEventList: TypeAlias = list[
    "aws_sdk_networkmanager.types.core_network_change_event.CoreNetworkChangeEvent"
]


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkChangeEventList) -> list:
    import aws_sdk_networkmanager.types.core_network_change_event

    out: list = []
    for item in value:
        out.append(
            aws_sdk_networkmanager.types.core_network_change_event.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CoreNetworkChangeEventList:
    import aws_sdk_networkmanager.types.core_network_change_event

    out: CoreNetworkChangeEventList = []
    for item in data:
        out.append(
            aws_sdk_networkmanager.types.core_network_change_event.deserialize_json(
                item
            )
        )
    return out
