"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ReloadTablesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string


class ReloadTablesResponse(TypedDict):
    replication_task_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) of the replication task. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReloadTablesResponse) -> dict:
    out: dict = {}
    if "replication_task_arn" in value:
        out["ReplicationTaskArn"] = value["replication_task_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReloadTablesResponse:
    out: ReloadTablesResponse = {}  # type: ignore[typeddict-item]
    if "ReplicationTaskArn" in data:
        out["replication_task_arn"] = data["ReplicationTaskArn"]
    return out
