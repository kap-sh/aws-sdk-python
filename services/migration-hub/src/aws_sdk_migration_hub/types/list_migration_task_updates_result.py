"""Generated from Smithy shape ``com.amazonaws.migrationhub#ListMigrationTaskUpdatesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migration_hub.types.migration_task_update_list
    import aws_sdk_migration_hub.types.token


class ListMigrationTaskUpdatesResult(TypedDict):
    next_token: NotRequired["aws_sdk_migration_hub.types.token.Token"]
    """<p>If the response includes a <code>NextToken</code> value, that means that there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. To retrieve the next page of results, call this API again and specify this <code>NextToken</code> value in the request. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.</p>"""
    migration_task_update_list: NotRequired[
        "aws_sdk_migration_hub.types.migration_task_update_list.MigrationTaskUpdateList"
    ]
    """<p>The list of migration-task updates.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMigrationTaskUpdatesResult) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "migration_task_update_list" in value:
        import aws_sdk_migration_hub.types.migration_task_update_list

        out["MigrationTaskUpdateList"] = (
            aws_sdk_migration_hub.types.migration_task_update_list.serialize_aws_json_1_1(
                value["migration_task_update_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMigrationTaskUpdatesResult:
    out: ListMigrationTaskUpdatesResult = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MigrationTaskUpdateList" in data:
        import aws_sdk_migration_hub.types.migration_task_update_list

        out["migration_task_update_list"] = (
            aws_sdk_migration_hub.types.migration_task_update_list.deserialize_aws_json_1_1(
                data["MigrationTaskUpdateList"]
            )
        )
    return out
