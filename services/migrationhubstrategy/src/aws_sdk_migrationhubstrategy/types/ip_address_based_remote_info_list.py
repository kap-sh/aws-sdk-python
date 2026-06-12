"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#IPAddressBasedRemoteInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.ip_address_based_remote_info

IPAddressBasedRemoteInfoList: TypeAlias = list[
    "aws_sdk_migrationhubstrategy.types.ip_address_based_remote_info.IPAddressBasedRemoteInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: IPAddressBasedRemoteInfoList) -> list:
    import aws_sdk_migrationhubstrategy.types.ip_address_based_remote_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_migrationhubstrategy.types.ip_address_based_remote_info.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> IPAddressBasedRemoteInfoList:
    import aws_sdk_migrationhubstrategy.types.ip_address_based_remote_info

    out: IPAddressBasedRemoteInfoList = []
    for item in data:
        out.append(
            aws_sdk_migrationhubstrategy.types.ip_address_based_remote_info.deserialize_json(
                item
            )
        )
    return out
