"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#VcenterBasedRemoteInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.vcenter_based_remote_info

VcenterBasedRemoteInfoList: TypeAlias = list[
    "aws_sdk_migrationhubstrategy.types.vcenter_based_remote_info.VcenterBasedRemoteInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: VcenterBasedRemoteInfoList) -> list:
    import aws_sdk_migrationhubstrategy.types.vcenter_based_remote_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_migrationhubstrategy.types.vcenter_based_remote_info.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> VcenterBasedRemoteInfoList:
    import aws_sdk_migrationhubstrategy.types.vcenter_based_remote_info

    out: VcenterBasedRemoteInfoList = []
    for item in data:
        out.append(
            aws_sdk_migrationhubstrategy.types.vcenter_based_remote_info.deserialize_json(
                item
            )
        )
    return out
