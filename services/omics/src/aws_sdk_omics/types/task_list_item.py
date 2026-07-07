"""Generated from Smithy shape ``com.amazonaws.omics#TaskListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.s3_uri_for_bucket_or_object
    import aws_sdk_omics.types.task_id
    import aws_sdk_omics.types.task_instance_type
    import aws_sdk_omics.types.task_name
    import aws_sdk_omics.types.task_status
    import aws_sdk_omics.types.task_timestamp


class TaskListItem(TypedDict, closed=True):
    task_id: NotRequired["aws_sdk_omics.types.task_id.TaskId"]
    """<p>The task's ID.</p>"""
    status: NotRequired["aws_sdk_omics.types.task_status.TaskStatus"]
    """<p>The task's status.</p>"""
    name: NotRequired["aws_sdk_omics.types.task_name.TaskName"]
    """<p>The task's name.</p>"""
    cpus: NotRequired["int"]
    """<p>The task's CPU count.</p>"""
    cache_hit: NotRequired["bool"]
    """<p>Set to true if Amazon Web Services HealthOmics found a matching entry in the run cache for this task.</p>"""
    cache_s3_uri: NotRequired[
        "aws_sdk_omics.types.s3_uri_for_bucket_or_object.S3UriForBucketOrObject"
    ]
    """<p>The S3 URI of the cache location.</p>"""
    memory: NotRequired["int"]
    """<p>The task's memory use in gigabyes.</p>"""
    creation_time: NotRequired["aws_sdk_omics.types.task_timestamp.TaskTimestamp"]
    """<p>When the task was created.</p>"""
    start_time: NotRequired["aws_sdk_omics.types.task_timestamp.TaskTimestamp"]
    """<p>When the task started.</p>"""
    stop_time: NotRequired["aws_sdk_omics.types.task_timestamp.TaskTimestamp"]
    """<p>When the task stopped.</p>"""
    gpus: NotRequired["int"]
    """<p> The number of Graphics Processing Units (GPU) specified for the task. </p>"""
    instance_type: NotRequired[
        "aws_sdk_omics.types.task_instance_type.TaskInstanceType"
    ]
    """<p> The instance type for a task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaskListItem) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    if "status" in value:
        out["status"] = value["status"]
    if "name" in value:
        out["name"] = value["name"]
    if "cpus" in value:
        out["cpus"] = value["cpus"]
    if "cache_hit" in value:
        out["cacheHit"] = value["cache_hit"]
    if "cache_s3_uri" in value:
        out["cacheS3Uri"] = value["cache_s3_uri"]
    if "memory" in value:
        out["memory"] = value["memory"]
    if "creation_time" in value:
        import aws_sdk_omics.types.task_timestamp

        out["creationTime"] = aws_sdk_omics.types.task_timestamp.serialize_json(
            value["creation_time"]
        )
    if "start_time" in value:
        import aws_sdk_omics.types.task_timestamp

        out["startTime"] = aws_sdk_omics.types.task_timestamp.serialize_json(
            value["start_time"]
        )
    if "stop_time" in value:
        import aws_sdk_omics.types.task_timestamp

        out["stopTime"] = aws_sdk_omics.types.task_timestamp.serialize_json(
            value["stop_time"]
        )
    if "gpus" in value:
        out["gpus"] = value["gpus"]
    if "instance_type" in value:
        out["instanceType"] = value["instance_type"]
    return out


def deserialize_json(data: dict) -> TaskListItem:
    out: TaskListItem = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    if "status" in data:
        out["status"] = data["status"]
    if "name" in data:
        out["name"] = data["name"]
    if "cpus" in data:
        out["cpus"] = data["cpus"]
    if "cacheHit" in data:
        out["cache_hit"] = data["cacheHit"]
    if "cacheS3Uri" in data:
        out["cache_s3_uri"] = data["cacheS3Uri"]
    if "memory" in data:
        out["memory"] = data["memory"]
    if "creationTime" in data:
        import aws_sdk_omics.types.task_timestamp

        out["creation_time"] = aws_sdk_omics.types.task_timestamp.deserialize_json(
            data["creationTime"]
        )
    if "startTime" in data:
        import aws_sdk_omics.types.task_timestamp

        out["start_time"] = aws_sdk_omics.types.task_timestamp.deserialize_json(
            data["startTime"]
        )
    if "stopTime" in data:
        import aws_sdk_omics.types.task_timestamp

        out["stop_time"] = aws_sdk_omics.types.task_timestamp.deserialize_json(
            data["stopTime"]
        )
    if "gpus" in data:
        out["gpus"] = data["gpus"]
    if "instanceType" in data:
        out["instance_type"] = data["instanceType"]
    return out
