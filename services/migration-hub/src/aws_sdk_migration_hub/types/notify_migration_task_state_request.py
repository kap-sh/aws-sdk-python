"""Generated from Smithy shape ``com.amazonaws.migrationhub#NotifyMigrationTaskStateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_migration_hub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_migration_hub.types.dry_run
    import aws_sdk_migration_hub.types.migration_task_name
    import aws_sdk_migration_hub.types.next_update_seconds
    import aws_sdk_migration_hub.types.progress_update_stream
    import aws_sdk_migration_hub.types.task
    import aws_sdk_migration_hub.types.update_date_time


class NotifyMigrationTaskStateRequest(TypedDict):
    progress_update_stream: (
        "aws_sdk_migration_hub.types.progress_update_stream.ProgressUpdateStream"
    )
    """<p>The name of the ProgressUpdateStream. </p>"""
    migration_task_name: (
        "aws_sdk_migration_hub.types.migration_task_name.MigrationTaskName"
    )
    """<p>Unique identifier that references the migration task. <i>Do not store personal data in this field.</i> </p>"""
    task: "aws_sdk_migration_hub.types.task.Task"
    """<p>Information about the task's progress and status.</p>"""
    update_date_time: "aws_sdk_migration_hub.types.update_date_time.UpdateDateTime"
    """<p>The timestamp when the task was gathered.</p>"""
    next_update_seconds: (
        "aws_sdk_migration_hub.types.next_update_seconds.NextUpdateSeconds"
    )
    """<p>Number of seconds after the UpdateDateTime within which the Migration Hub can expect an update. If Migration Hub does not receive an update within the specified interval, then the migration task will be considered stale.</p>"""
    dry_run: "aws_sdk_migration_hub.types.dry_run.DryRun"
    """<p>Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotifyMigrationTaskStateRequest) -> dict:
    out: dict = {}
    out["ProgressUpdateStream"] = value["progress_update_stream"]
    out["MigrationTaskName"] = value["migration_task_name"]
    import aws_sdk_migration_hub.types.task

    out["Task"] = aws_sdk_migration_hub.types.task.serialize_aws_json_1_1(value["task"])
    import aws_sdk_migration_hub.types.update_date_time

    out["UpdateDateTime"] = (
        aws_sdk_migration_hub.types.update_date_time.serialize_aws_json_1_1(
            value["update_date_time"]
        )
    )
    out["NextUpdateSeconds"] = value.get("next_update_seconds", 0)
    out["DryRun"] = value.get("dry_run", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> NotifyMigrationTaskStateRequest:
    out: NotifyMigrationTaskStateRequest = {}  # type: ignore[typeddict-item]
    if "ProgressUpdateStream" in data:
        out["progress_update_stream"] = data["ProgressUpdateStream"]
    else:
        raise DeserializationError(
            "NotifyMigrationTaskStateRequest.progress_update_stream required"
        )
    if "MigrationTaskName" in data:
        out["migration_task_name"] = data["MigrationTaskName"]
    else:
        raise DeserializationError(
            "NotifyMigrationTaskStateRequest.migration_task_name required"
        )
    if "Task" in data:
        import aws_sdk_migration_hub.types.task

        out["task"] = aws_sdk_migration_hub.types.task.deserialize_aws_json_1_1(
            data["Task"]
        )
    else:
        raise DeserializationError("NotifyMigrationTaskStateRequest.task required")
    if "UpdateDateTime" in data:
        import aws_sdk_migration_hub.types.update_date_time

        out["update_date_time"] = (
            aws_sdk_migration_hub.types.update_date_time.deserialize_aws_json_1_1(
                data["UpdateDateTime"]
            )
        )
    else:
        raise DeserializationError(
            "NotifyMigrationTaskStateRequest.update_date_time required"
        )
    if "NextUpdateSeconds" in data:
        out["next_update_seconds"] = data["NextUpdateSeconds"]
    else:
        out["next_update_seconds"] = 0
    if "DryRun" in data:
        out["dry_run"] = data["DryRun"]
    else:
        out["dry_run"] = False
    return out
