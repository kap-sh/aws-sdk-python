"""Generated from Smithy shape ``com.amazonaws.datapipeline#ReportTaskRunnerHeartbeatInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_data_pipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.id
    import aws_sdk_data_pipeline.types.string


class ReportTaskRunnerHeartbeatInput(TypedDict, closed=True):
    taskrunner_id: "aws_sdk_data_pipeline.types.id.id"
    """<p>The ID of the task runner. This value should be unique across your AWS account. In the case of AWS Data Pipeline Task Runner launched on a resource managed by AWS Data Pipeline, the web service provides a unique identifier when it launches the application. If you have written a custom task runner, you should assign a unique identifier for the task runner.</p>"""
    worker_group: NotRequired["aws_sdk_data_pipeline.types.string.string"]
    """<p>The type of task the task runner is configured to accept and process. The worker group is set as a field on objects in the pipeline when they are created. You can only specify a single value for <code>workerGroup</code>. There are no wildcard values permitted in <code>workerGroup</code>; the string must be an exact, case-sensitive, match.</p>"""
    hostname: NotRequired["aws_sdk_data_pipeline.types.id.id"]
    """<p>The public DNS name of the task runner.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportTaskRunnerHeartbeatInput) -> dict:
    out: dict = {}
    out["taskrunnerId"] = value["taskrunner_id"]
    if "worker_group" in value:
        out["workerGroup"] = value["worker_group"]
    if "hostname" in value:
        out["hostname"] = value["hostname"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReportTaskRunnerHeartbeatInput:
    out: ReportTaskRunnerHeartbeatInput = {}  # type: ignore[typeddict-item]
    if "taskrunnerId" in data:
        out["taskrunner_id"] = data["taskrunnerId"]
    else:
        raise DeserializationError(
            "ReportTaskRunnerHeartbeatInput.taskrunner_id required"
        )
    if "workerGroup" in data:
        out["worker_group"] = data["workerGroup"]
    if "hostname" in data:
        out["hostname"] = data["hostname"]
    return out
