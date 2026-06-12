"""Generated from Smithy shape ``com.amazonaws.datapipeline#SetTaskStatusInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_data_pipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.error_message
    import aws_sdk_data_pipeline.types.string
    import aws_sdk_data_pipeline.types.task_id
    import aws_sdk_data_pipeline.types.task_status


class SetTaskStatusInput(TypedDict):
    task_id: "aws_sdk_data_pipeline.types.task_id.taskId"
    """<p>The ID of the task assigned to the task runner. This value is provided in the response for <a>PollForTask</a>.</p>"""
    task_status: "aws_sdk_data_pipeline.types.task_status.TaskStatus"
    """<p>If <code>FINISHED</code>, the task successfully completed. If <code>FAILED</code>, the task ended unsuccessfully. Preconditions use false.</p>"""
    error_id: NotRequired["aws_sdk_data_pipeline.types.string.string"]
    """<p>If an error occurred during the task, this value specifies the error code. This value is set on the physical attempt object. It is used to display error information to the user. It should not start with string \"Service_\" which is reserved by the system.</p>"""
    error_message: NotRequired["aws_sdk_data_pipeline.types.error_message.errorMessage"]
    """<p>If an error occurred during the task, this value specifies a text description of the error. This value is set on the physical attempt object. It is used to display error information to the user. The web service does not parse this value.</p>"""
    error_stack_trace: NotRequired["aws_sdk_data_pipeline.types.string.string"]
    """<p>If an error occurred during the task, this value specifies the stack trace associated with the error. This value is set on the physical attempt object. It is used to display error information to the user. The web service does not parse this value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetTaskStatusInput) -> dict:
    out: dict = {}
    out["taskId"] = value["task_id"]
    import aws_sdk_data_pipeline.types.task_status

    out["taskStatus"] = aws_sdk_data_pipeline.types.task_status.serialize_aws_json_1_1(
        value["task_status"]
    )
    if "error_id" in value:
        out["errorId"] = value["error_id"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "error_stack_trace" in value:
        out["errorStackTrace"] = value["error_stack_trace"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SetTaskStatusInput:
    out: SetTaskStatusInput = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    else:
        raise DeserializationError("SetTaskStatusInput.task_id required")
    if "taskStatus" in data:
        import aws_sdk_data_pipeline.types.task_status

        out["task_status"] = (
            aws_sdk_data_pipeline.types.task_status.deserialize_aws_json_1_1(
                data["taskStatus"]
            )
        )
    else:
        raise DeserializationError("SetTaskStatusInput.task_status required")
    if "errorId" in data:
        out["error_id"] = data["errorId"]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    if "errorStackTrace" in data:
        out["error_stack_trace"] = data["errorStackTrace"]
    return out
