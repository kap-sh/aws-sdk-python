"""Generated from Smithy shape ``com.amazonaws.greengrass#__listOfConnectivityInfo``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_greengrass.types.connectivity_info

__listOfConnectivityInfo: TypeAlias = list[
    "capo_greengrass.types.connectivity_info.ConnectivityInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfConnectivityInfo) -> list:
    import capo_greengrass.types.connectivity_info

    out: list = []
    for item in value:
        out.append(capo_greengrass.types.connectivity_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfConnectivityInfo:
    import capo_greengrass.types.connectivity_info

    out: __listOfConnectivityInfo = []
    for item in data:
        out.append(capo_greengrass.types.connectivity_info.deserialize_json(item))
    return out
