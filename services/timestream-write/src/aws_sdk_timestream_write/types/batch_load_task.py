"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#BatchLoadTask``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.batch_load_status
    import aws_sdk_timestream_write.types.batch_load_task_id
    import aws_sdk_timestream_write.types.date
    import aws_sdk_timestream_write.types.resource_name


class BatchLoadTask(TypedDict):
    task_id: NotRequired[
        "aws_sdk_timestream_write.types.batch_load_task_id.BatchLoadTaskId"
    ]
    """<p>The ID of the batch load task.</p>"""
    task_status: NotRequired[
        "aws_sdk_timestream_write.types.batch_load_status.BatchLoadStatus"
    ]
    """<p>Status of the batch load task.</p>"""
    database_name: NotRequired[
        "aws_sdk_timestream_write.types.resource_name.ResourceName"
    ]
    """<p>Database name for the database into which a batch load task loads data.</p>"""
    table_name: NotRequired["aws_sdk_timestream_write.types.resource_name.ResourceName"]
    """<p>Table name for the table into which a batch load task loads data.</p>"""
    creation_time: NotRequired["aws_sdk_timestream_write.types.date.Date"]
    """<p>The time when the Timestream batch load task was created.</p>"""
    last_updated_time: NotRequired["aws_sdk_timestream_write.types.date.Date"]
    """<p>The time when the Timestream batch load task was last updated.</p>"""
    resumable_until: NotRequired["aws_sdk_timestream_write.types.date.Date"]
    """<p> </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchLoadTask) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["TaskId"] = value["task_id"]
    if "task_status" in value:
        import aws_sdk_timestream_write.types.batch_load_status

        out["TaskStatus"] = (
            aws_sdk_timestream_write.types.batch_load_status.serialize_aws_json_1_0(
                value["task_status"]
            )
        )
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "creation_time" in value:
        import aws_sdk_timestream_write.types.date

        out["CreationTime"] = (
            aws_sdk_timestream_write.types.date.serialize_aws_json_1_0(
                value["creation_time"]
            )
        )
    if "last_updated_time" in value:
        import aws_sdk_timestream_write.types.date

        out["LastUpdatedTime"] = (
            aws_sdk_timestream_write.types.date.serialize_aws_json_1_0(
                value["last_updated_time"]
            )
        )
    if "resumable_until" in value:
        import aws_sdk_timestream_write.types.date

        out["ResumableUntil"] = (
            aws_sdk_timestream_write.types.date.serialize_aws_json_1_0(
                value["resumable_until"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchLoadTask:
    out: BatchLoadTask = {}  # type: ignore[typeddict-item]
    if "TaskId" in data:
        out["task_id"] = data["TaskId"]
    if "TaskStatus" in data:
        import aws_sdk_timestream_write.types.batch_load_status

        out["task_status"] = (
            aws_sdk_timestream_write.types.batch_load_status.deserialize_aws_json_1_0(
                data["TaskStatus"]
            )
        )
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    if "CreationTime" in data:
        import aws_sdk_timestream_write.types.date

        out["creation_time"] = (
            aws_sdk_timestream_write.types.date.deserialize_aws_json_1_0(
                data["CreationTime"]
            )
        )
    if "LastUpdatedTime" in data:
        import aws_sdk_timestream_write.types.date

        out["last_updated_time"] = (
            aws_sdk_timestream_write.types.date.deserialize_aws_json_1_0(
                data["LastUpdatedTime"]
            )
        )
    if "ResumableUntil" in data:
        import aws_sdk_timestream_write.types.date

        out["resumable_until"] = (
            aws_sdk_timestream_write.types.date.deserialize_aws_json_1_0(
                data["ResumableUntil"]
            )
        )
    return out
