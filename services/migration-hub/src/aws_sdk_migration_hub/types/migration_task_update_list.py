"""Generated from Smithy shape ``com.amazonaws.migrationhub#MigrationTaskUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_migration_hub.types.migration_task_update

MigrationTaskUpdateList: TypeAlias = list[
    "aws_sdk_migration_hub.types.migration_task_update.MigrationTaskUpdate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MigrationTaskUpdateList) -> list:
    import aws_sdk_migration_hub.types.migration_task_update

    out: list = []
    for item in value:
        out.append(
            aws_sdk_migration_hub.types.migration_task_update.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MigrationTaskUpdateList:
    import aws_sdk_migration_hub.types.migration_task_update

    out: MigrationTaskUpdateList = []
    for item in data:
        out.append(
            aws_sdk_migration_hub.types.migration_task_update.deserialize_aws_json_1_1(
                item
            )
        )
    return out
