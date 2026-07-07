"""Generated from Smithy shape ``com.amazonaws.omics#GetRunTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.image_details
    import aws_sdk_omics.types.s3_uri_for_bucket_or_object
    import aws_sdk_omics.types.task_failure_reason
    import aws_sdk_omics.types.task_id
    import aws_sdk_omics.types.task_instance_type
    import aws_sdk_omics.types.task_log_stream
    import aws_sdk_omics.types.task_name
    import aws_sdk_omics.types.task_status
    import aws_sdk_omics.types.task_status_message
    import aws_sdk_omics.types.task_timestamp


class GetRunTaskResponse(TypedDict, closed=True):
    task_id: NotRequired["aws_sdk_omics.types.task_id.TaskId"]
    """<p>The task's ID.</p>"""
    status: NotRequired["aws_sdk_omics.types.task_status.TaskStatus"]
    """<p>The task's status.</p>"""
    name: NotRequired["aws_sdk_omics.types.task_name.TaskName"]
    """<p>The task's name.</p>"""
    cpus: NotRequired["int"]
    """<p>The task's CPU usage.</p>"""
    cache_hit: NotRequired["bool"]
    """<p>Set to true if Amazon Web Services HealthOmics found a matching entry in the run cache for this task.</p>"""
    cache_s3_uri: NotRequired[
        "aws_sdk_omics.types.s3_uri_for_bucket_or_object.S3UriForBucketOrObject"
    ]
    """<p>The S3 URI of the cache location.</p>"""
    memory: NotRequired["int"]
    """<p>The task's memory use in gigabytes.</p>"""
    creation_time: NotRequired["aws_sdk_omics.types.task_timestamp.TaskTimestamp"]
    """<p>When the task was created.</p>"""
    start_time: NotRequired["aws_sdk_omics.types.task_timestamp.TaskTimestamp"]
    """<p>The task's start time.</p>"""
    stop_time: NotRequired["aws_sdk_omics.types.task_timestamp.TaskTimestamp"]
    """<p>The task's stop time.</p>"""
    status_message: NotRequired[
        "aws_sdk_omics.types.task_status_message.TaskStatusMessage"
    ]
    """<p>The task's status message.</p>"""
    log_stream: NotRequired["aws_sdk_omics.types.task_log_stream.TaskLogStream"]
    """<p>The task's log stream.</p>"""
    gpus: NotRequired["int"]
    """<p>The number of Graphics Processing Units (GPU) specified in the task.</p>"""
    instance_type: NotRequired[
        "aws_sdk_omics.types.task_instance_type.TaskInstanceType"
    ]
    """<p>The instance type for a task.</p>"""
    failure_reason: NotRequired[
        "aws_sdk_omics.types.task_failure_reason.TaskFailureReason"
    ]
    """<p>The reason a task has failed.</p>"""
    image_details: NotRequired["aws_sdk_omics.types.image_details.ImageDetails"]
    """<p>Details about the container image that this task uses.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRunTaskResponse) -> dict:
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
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "log_stream" in value:
        out["logStream"] = value["log_stream"]
    if "gpus" in value:
        out["gpus"] = value["gpus"]
    if "instance_type" in value:
        out["instanceType"] = value["instance_type"]
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    if "image_details" in value:
        import aws_sdk_omics.types.image_details

        out["imageDetails"] = aws_sdk_omics.types.image_details.serialize_json(
            value["image_details"]
        )
    return out


def deserialize_json(data: dict) -> GetRunTaskResponse:
    out: GetRunTaskResponse = {}  # type: ignore[typeddict-item]
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
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "logStream" in data:
        out["log_stream"] = data["logStream"]
    if "gpus" in data:
        out["gpus"] = data["gpus"]
    if "instanceType" in data:
        out["instance_type"] = data["instanceType"]
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    if "imageDetails" in data:
        import aws_sdk_omics.types.image_details

        out["image_details"] = aws_sdk_omics.types.image_details.deserialize_json(
            data["imageDetails"]
        )
    return out
