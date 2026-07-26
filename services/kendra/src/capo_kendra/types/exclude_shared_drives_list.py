"""Generated from Smithy shape ``com.amazonaws.kendra#ExcludeSharedDrivesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.shared_drive_id

ExcludeSharedDrivesList: TypeAlias = list[
    "capo_kendra.types.shared_drive_id.SharedDriveId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExcludeSharedDrivesList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ExcludeSharedDrivesList:
    return list(data)
