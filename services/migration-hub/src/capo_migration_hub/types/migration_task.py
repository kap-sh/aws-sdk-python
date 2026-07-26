"""Generated from Smithy shape ``com.amazonaws.migrationhub#MigrationTask``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migration_hub.types.latest_resource_attribute_list
    import capo_migration_hub.types.migration_task_name
    import capo_migration_hub.types.progress_update_stream
    import capo_migration_hub.types.task
    import capo_migration_hub.types.update_date_time


class MigrationTask(TypedDict, closed=True):
    progress_update_stream: NotRequired[
        "capo_migration_hub.types.progress_update_stream.ProgressUpdateStream"
    ]
    """<p>A name that identifies the vendor of the migration tool being used.</p>"""
    migration_task_name: NotRequired[
        "capo_migration_hub.types.migration_task_name.MigrationTaskName"
    ]
    """<p>Unique identifier that references the migration task. <i>Do not store personal data in this field.</i> </p>"""
    task: NotRequired["capo_migration_hub.types.task.Task"]
    """<p>Task object encapsulating task information.</p>"""
    update_date_time: NotRequired[
        "capo_migration_hub.types.update_date_time.UpdateDateTime"
    ]
    """<p>The timestamp when the task was gathered.</p>"""
    resource_attribute_list: NotRequired[
        "capo_migration_hub.types.latest_resource_attribute_list.LatestResourceAttributeList"
    ]
    """<p>Information about the resource that is being migrated. This data will be used to map the task to a resource in the Application Discovery Service repository.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MigrationTask) -> dict:
    out: dict = {}
    if "progress_update_stream" in value:
        out["ProgressUpdateStream"] = value["progress_update_stream"]
    if "migration_task_name" in value:
        out["MigrationTaskName"] = value["migration_task_name"]
    if "task" in value:
        import capo_migration_hub.types.task

        out["Task"] = capo_migration_hub.types.task.serialize_aws_json_1_1(
            value["task"]
        )
    if "update_date_time" in value:
        import capo_migration_hub.types.update_date_time

        out["UpdateDateTime"] = (
            capo_migration_hub.types.update_date_time.serialize_aws_json_1_1(
                value["update_date_time"]
            )
        )
    if "resource_attribute_list" in value:
        import capo_migration_hub.types.latest_resource_attribute_list

        out["ResourceAttributeList"] = (
            capo_migration_hub.types.latest_resource_attribute_list.serialize_aws_json_1_1(
                value["resource_attribute_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MigrationTask:
    out: MigrationTask = {}  # type: ignore[typeddict-item]
    if "ProgressUpdateStream" in data:
        out["progress_update_stream"] = data["ProgressUpdateStream"]
    if "MigrationTaskName" in data:
        out["migration_task_name"] = data["MigrationTaskName"]
    if "Task" in data:
        import capo_migration_hub.types.task

        out["task"] = capo_migration_hub.types.task.deserialize_aws_json_1_1(
            data["Task"]
        )
    if "UpdateDateTime" in data:
        import capo_migration_hub.types.update_date_time

        out["update_date_time"] = (
            capo_migration_hub.types.update_date_time.deserialize_aws_json_1_1(
                data["UpdateDateTime"]
            )
        )
    if "ResourceAttributeList" in data:
        import capo_migration_hub.types.latest_resource_attribute_list

        out["resource_attribute_list"] = (
            capo_migration_hub.types.latest_resource_attribute_list.deserialize_aws_json_1_1(
                data["ResourceAttributeList"]
            )
        )
    return out
