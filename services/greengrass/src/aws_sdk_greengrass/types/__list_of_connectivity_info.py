"""Generated from Smithy shape ``com.amazonaws.greengrass#__listOfConnectivityInfo``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.connectivity_info

__listOfConnectivityInfo: TypeAlias = list[
    "aws_sdk_greengrass.types.connectivity_info.ConnectivityInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfConnectivityInfo) -> list:
    import aws_sdk_greengrass.types.connectivity_info

    out: list = []
    for item in value:
        out.append(aws_sdk_greengrass.types.connectivity_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfConnectivityInfo:
    import aws_sdk_greengrass.types.connectivity_info

    out: __listOfConnectivityInfo = []
    for item in data:
        out.append(aws_sdk_greengrass.types.connectivity_info.deserialize_json(item))
    return out
