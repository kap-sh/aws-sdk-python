"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeleteLogGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.log_group_name


class DeleteLogGroupRequest(TypedDict, closed=True):
    log_group_name: "aws_sdk_cloudwatch_logs.types.log_group_name.LogGroupName"
    """<p>The name of the log group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteLogGroupRequest) -> dict:
    out: dict = {}
    out["logGroupName"] = value["log_group_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteLogGroupRequest:
    out: DeleteLogGroupRequest = {}  # type: ignore[typeddict-item]
    if "logGroupName" in data:
        out["log_group_name"] = data["logGroupName"]
    else:
        raise DeserializationError("DeleteLogGroupRequest.log_group_name required")
    return out
