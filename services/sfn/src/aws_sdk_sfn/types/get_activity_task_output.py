"""Generated from Smithy shape ``com.amazonaws.sfn#GetActivityTaskOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sfn.types.sensitive_data_job_input
    import aws_sdk_sfn.types.task_token


class GetActivityTaskOutput(TypedDict):
    task_token: NotRequired["aws_sdk_sfn.types.task_token.TaskToken"]
    """<p>A token that identifies the scheduled task. This token must be copied and included in subsequent calls to <a>SendTaskHeartbeat</a>, <a>SendTaskSuccess</a> or <a>SendTaskFailure</a> in order to report the progress or completion of the task.</p>"""
    input: NotRequired[
        "aws_sdk_sfn.types.sensitive_data_job_input.SensitiveDataJobInput"
    ]
    """<p>The string that contains the JSON input data for the task. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetActivityTaskOutput) -> dict:
    out: dict = {}
    if "task_token" in value:
        out["taskToken"] = value["task_token"]
    if "input" in value:
        out["input"] = value["input"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetActivityTaskOutput:
    out: GetActivityTaskOutput = {}  # type: ignore[typeddict-item]
    if "taskToken" in data:
        out["task_token"] = data["taskToken"]
    if "input" in data:
        out["input"] = data["input"]
    return out
