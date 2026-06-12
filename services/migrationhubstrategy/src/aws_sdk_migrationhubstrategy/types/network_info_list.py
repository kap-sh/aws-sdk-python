"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#NetworkInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.network_info

NetworkInfoList: TypeAlias = list[
    "aws_sdk_migrationhubstrategy.types.network_info.NetworkInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkInfoList) -> list:
    import aws_sdk_migrationhubstrategy.types.network_info

    out: list = []
    for item in value:
        out.append(aws_sdk_migrationhubstrategy.types.network_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> NetworkInfoList:
    import aws_sdk_migrationhubstrategy.types.network_info

    out: NetworkInfoList = []
    for item in data:
        out.append(
            aws_sdk_migrationhubstrategy.types.network_info.deserialize_json(item)
        )
    return out
