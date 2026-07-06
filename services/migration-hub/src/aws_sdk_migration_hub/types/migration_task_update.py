"""Generated from Smithy shape ``com.amazonaws.migrationhub#MigrationTaskUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migration_hub.types.task
    import aws_sdk_migration_hub.types.update_date_time
    import aws_sdk_migration_hub.types.update_type


class MigrationTaskUpdate(TypedDict, closed=True):
    update_date_time: NotRequired[
        "aws_sdk_migration_hub.types.update_date_time.UpdateDateTime"
    ]
    """<p>The timestamp for the update.</p>"""
    update_type: NotRequired["aws_sdk_migration_hub.types.update_type.UpdateType"]
    """<p>The type of the update.</p>"""
    migration_task_state: NotRequired["aws_sdk_migration_hub.types.task.Task"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MigrationTaskUpdate) -> dict:
    out: dict = {}
    if "update_date_time" in value:
        import aws_sdk_migration_hub.types.update_date_time

        out["UpdateDateTime"] = (
            aws_sdk_migration_hub.types.update_date_time.serialize_aws_json_1_1(
                value["update_date_time"]
            )
        )
    if "update_type" in value:
        import aws_sdk_migration_hub.types.update_type

        out["UpdateType"] = (
            aws_sdk_migration_hub.types.update_type.serialize_aws_json_1_1(
                value["update_type"]
            )
        )
    if "migration_task_state" in value:
        import aws_sdk_migration_hub.types.task

        out["MigrationTaskState"] = (
            aws_sdk_migration_hub.types.task.serialize_aws_json_1_1(
                value["migration_task_state"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MigrationTaskUpdate:
    out: MigrationTaskUpdate = {}  # type: ignore[typeddict-item]
    if "UpdateDateTime" in data:
        import aws_sdk_migration_hub.types.update_date_time

        out["update_date_time"] = (
            aws_sdk_migration_hub.types.update_date_time.deserialize_aws_json_1_1(
                data["UpdateDateTime"]
            )
        )
    if "UpdateType" in data:
        import aws_sdk_migration_hub.types.update_type

        out["update_type"] = (
            aws_sdk_migration_hub.types.update_type.deserialize_aws_json_1_1(
                data["UpdateType"]
            )
        )
    if "MigrationTaskState" in data:
        import aws_sdk_migration_hub.types.task

        out["migration_task_state"] = (
            aws_sdk_migration_hub.types.task.deserialize_aws_json_1_1(
                data["MigrationTaskState"]
            )
        )
    return out
