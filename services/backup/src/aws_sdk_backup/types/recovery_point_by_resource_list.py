"""Generated from Smithy shape ``com.amazonaws.backup#RecoveryPointByResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backup.types.recovery_point_by_resource

RecoveryPointByResourceList: TypeAlias = list[
    "aws_sdk_backup.types.recovery_point_by_resource.RecoveryPointByResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryPointByResourceList) -> list:
    import aws_sdk_backup.types.recovery_point_by_resource

    out: list = []
    for item in value:
        out.append(aws_sdk_backup.types.recovery_point_by_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecoveryPointByResourceList:
    import aws_sdk_backup.types.recovery_point_by_resource

    out: RecoveryPointByResourceList = []
    for item in data:
        out.append(
            aws_sdk_backup.types.recovery_point_by_resource.deserialize_json(item)
        )
    return out
