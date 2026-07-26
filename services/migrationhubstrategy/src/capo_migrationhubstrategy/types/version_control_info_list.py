"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#VersionControlInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.version_control_info

VersionControlInfoList: TypeAlias = list[
    "capo_migrationhubstrategy.types.version_control_info.VersionControlInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: VersionControlInfoList) -> list:
    import capo_migrationhubstrategy.types.version_control_info

    out: list = []
    for item in value:
        out.append(
            capo_migrationhubstrategy.types.version_control_info.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> VersionControlInfoList:
    import capo_migrationhubstrategy.types.version_control_info

    out: VersionControlInfoList = []
    for item in data:
        out.append(
            capo_migrationhubstrategy.types.version_control_info.deserialize_json(item)
        )
    return out
