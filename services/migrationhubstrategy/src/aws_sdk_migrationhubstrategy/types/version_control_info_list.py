"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#VersionControlInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.version_control_info

VersionControlInfoList: TypeAlias = list[
    "aws_sdk_migrationhubstrategy.types.version_control_info.VersionControlInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: VersionControlInfoList) -> list:
    import aws_sdk_migrationhubstrategy.types.version_control_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_migrationhubstrategy.types.version_control_info.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> VersionControlInfoList:
    import aws_sdk_migrationhubstrategy.types.version_control_info

    out: VersionControlInfoList = []
    for item in data:
        out.append(
            aws_sdk_migrationhubstrategy.types.version_control_info.deserialize_json(
                item
            )
        )
    return out
