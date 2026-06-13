"""Generated from Smithy shape ``com.amazonaws.internetmonitor#NetworkList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_internetmonitor.types.network

NetworkList: TypeAlias = list["aws_sdk_internetmonitor.types.network.Network"]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkList) -> list:
    import aws_sdk_internetmonitor.types.network

    out: list = []
    for item in value:
        out.append(aws_sdk_internetmonitor.types.network.serialize_json(item))
    return out


def deserialize_json(data: list) -> NetworkList:
    import aws_sdk_internetmonitor.types.network

    out: NetworkList = []
    for item in data:
        out.append(aws_sdk_internetmonitor.types.network.deserialize_json(item))
    return out
