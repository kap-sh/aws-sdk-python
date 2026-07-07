"""Generated from Smithy shape ``com.amazonaws.datasync#DescribeTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datasync.types.task_arn


class DescribeTaskRequest(TypedDict, closed=True):
    task_arn: "aws_sdk_datasync.types.task_arn.TaskArn"
    """<p>Specifies the Amazon Resource Name (ARN) of the transfer task that you want information about.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTaskRequest) -> dict:
    out: dict = {}
    out["TaskArn"] = value["task_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTaskRequest:
    out: DescribeTaskRequest = {}  # type: ignore[typeddict-item]
    if "TaskArn" in data:
        out["task_arn"] = data["TaskArn"]
    else:
        raise DeserializationError("DescribeTaskRequest.task_arn required")
    return out
