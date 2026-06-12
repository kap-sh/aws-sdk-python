"""Generated from Smithy shape ``com.amazonaws.migrationhub#MigrationTaskSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_migration_hub.types.migration_task_summary

MigrationTaskSummaryList: TypeAlias = list[
    "aws_sdk_migration_hub.types.migration_task_summary.MigrationTaskSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MigrationTaskSummaryList) -> list:
    import aws_sdk_migration_hub.types.migration_task_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_migration_hub.types.migration_task_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MigrationTaskSummaryList:
    import aws_sdk_migration_hub.types.migration_task_summary

    out: MigrationTaskSummaryList = []
    for item in data:
        out.append(
            aws_sdk_migration_hub.types.migration_task_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
