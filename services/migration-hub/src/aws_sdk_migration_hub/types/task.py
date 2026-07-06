"""Generated from Smithy shape ``com.amazonaws.migrationhub#Task``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_migration_hub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_migration_hub.types.progress_percent
    import aws_sdk_migration_hub.types.status
    import aws_sdk_migration_hub.types.status_detail


class Task(TypedDict, closed=True):
    status: "aws_sdk_migration_hub.types.status.Status"
    """<p>Status of the task - Not Started, In-Progress, Complete.</p>"""
    status_detail: NotRequired["aws_sdk_migration_hub.types.status_detail.StatusDetail"]
    """<p>Details of task status as notified by a migration tool. A tool might use this field to provide clarifying information about the status that is unique to that tool or that explains an error state.</p>"""
    progress_percent: NotRequired[
        "aws_sdk_migration_hub.types.progress_percent.ProgressPercent"
    ]
    """<p>Indication of the percentage completion of the task.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Task) -> dict:
    out: dict = {}
    import aws_sdk_migration_hub.types.status

    out["Status"] = aws_sdk_migration_hub.types.status.serialize_aws_json_1_1(
        value["status"]
    )
    if "status_detail" in value:
        out["StatusDetail"] = value["status_detail"]
    if "progress_percent" in value:
        out["ProgressPercent"] = value["progress_percent"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Task:
    out: Task = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_migration_hub.types.status

        out["status"] = aws_sdk_migration_hub.types.status.deserialize_aws_json_1_1(
            data["Status"]
        )
    else:
        raise DeserializationError("Task.status required")
    if "StatusDetail" in data:
        out["status_detail"] = data["StatusDetail"]
    if "ProgressPercent" in data:
        out["progress_percent"] = data["ProgressPercent"]
    return out
