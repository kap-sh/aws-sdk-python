"""Generated from Smithy shape ``com.amazonaws.backupsearch#RecoveryPointArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backupsearch.types.recovery_point

RecoveryPointArnList: TypeAlias = list[
    "aws_sdk_backupsearch.types.recovery_point.RecoveryPoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryPointArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> RecoveryPointArnList:
    return list(data)
