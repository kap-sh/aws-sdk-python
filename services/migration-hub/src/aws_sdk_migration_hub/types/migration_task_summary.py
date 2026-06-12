"""Generated from Smithy shape ``com.amazonaws.migrationhub#MigrationTaskSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migration_hub.types.migration_task_name
    import aws_sdk_migration_hub.types.progress_percent
    import aws_sdk_migration_hub.types.progress_update_stream
    import aws_sdk_migration_hub.types.status
    import aws_sdk_migration_hub.types.status_detail
    import aws_sdk_migration_hub.types.update_date_time


class MigrationTaskSummary(TypedDict):
    progress_update_stream: NotRequired[
        "aws_sdk_migration_hub.types.progress_update_stream.ProgressUpdateStream"
    ]
    """<p>An AWS resource used for access control. It should uniquely identify the migration tool as it is used for all updates made by the tool.</p>"""
    migration_task_name: NotRequired[
        "aws_sdk_migration_hub.types.migration_task_name.MigrationTaskName"
    ]
    """<p>Unique identifier that references the migration task. <i>Do not store personal data in this field.</i> </p>"""
    status: NotRequired["aws_sdk_migration_hub.types.status.Status"]
    """<p>Status of the task.</p>"""
    progress_percent: NotRequired[
        "aws_sdk_migration_hub.types.progress_percent.ProgressPercent"
    ]
    """<p>Indication of the percentage completion of the task.</p>"""
    status_detail: NotRequired["aws_sdk_migration_hub.types.status_detail.StatusDetail"]
    """<p>Detail information of what is being done within the overall status state.</p>"""
    update_date_time: NotRequired[
        "aws_sdk_migration_hub.types.update_date_time.UpdateDateTime"
    ]
    """<p>The timestamp when the task was gathered.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MigrationTaskSummary) -> dict:
    out: dict = {}
    if "progress_update_stream" in value:
        out["ProgressUpdateStream"] = value["progress_update_stream"]
    if "migration_task_name" in value:
        out["MigrationTaskName"] = value["migration_task_name"]
    if "status" in value:
        import aws_sdk_migration_hub.types.status

        out["Status"] = aws_sdk_migration_hub.types.status.serialize_aws_json_1_1(
            value["status"]
        )
    if "progress_percent" in value:
        out["ProgressPercent"] = value["progress_percent"]
    if "status_detail" in value:
        out["StatusDetail"] = value["status_detail"]
    if "update_date_time" in value:
        import aws_sdk_migration_hub.types.update_date_time

        out["UpdateDateTime"] = (
            aws_sdk_migration_hub.types.update_date_time.serialize_aws_json_1_1(
                value["update_date_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MigrationTaskSummary:
    out: MigrationTaskSummary = {}  # type: ignore[typeddict-item]
    if "ProgressUpdateStream" in data:
        out["progress_update_stream"] = data["ProgressUpdateStream"]
    if "MigrationTaskName" in data:
        out["migration_task_name"] = data["MigrationTaskName"]
    if "Status" in data:
        import aws_sdk_migration_hub.types.status

        out["status"] = aws_sdk_migration_hub.types.status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "ProgressPercent" in data:
        out["progress_percent"] = data["ProgressPercent"]
    if "StatusDetail" in data:
        out["status_detail"] = data["StatusDetail"]
    if "UpdateDateTime" in data:
        import aws_sdk_migration_hub.types.update_date_time

        out["update_date_time"] = (
            aws_sdk_migration_hub.types.update_date_time.deserialize_aws_json_1_1(
                data["UpdateDateTime"]
            )
        )
    return out
