"""Generated from Smithy shape ``com.amazonaws.migrationhub#ListMigrationTasksResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migration_hub.types.migration_task_summary_list
    import aws_sdk_migration_hub.types.token


class ListMigrationTasksResult(TypedDict):
    next_token: NotRequired["aws_sdk_migration_hub.types.token.Token"]
    """<p>If there are more migration tasks than the max result, return the next token to be passed to the next call as a bookmark of where to start from.</p>"""
    migration_task_summary_list: NotRequired[
        "aws_sdk_migration_hub.types.migration_task_summary_list.MigrationTaskSummaryList"
    ]
    """<p>Lists the migration task's summary which includes: <code>MigrationTaskName</code>, <code>ProgressPercent</code>, <code>ProgressUpdateStream</code>, <code>Status</code>, and the <code>UpdateDateTime</code> for each task.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMigrationTasksResult) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "migration_task_summary_list" in value:
        import aws_sdk_migration_hub.types.migration_task_summary_list

        out["MigrationTaskSummaryList"] = (
            aws_sdk_migration_hub.types.migration_task_summary_list.serialize_aws_json_1_1(
                value["migration_task_summary_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMigrationTasksResult:
    out: ListMigrationTasksResult = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MigrationTaskSummaryList" in data:
        import aws_sdk_migration_hub.types.migration_task_summary_list

        out["migration_task_summary_list"] = (
            aws_sdk_migration_hub.types.migration_task_summary_list.deserialize_aws_json_1_1(
                data["MigrationTaskSummaryList"]
            )
        )
    return out
