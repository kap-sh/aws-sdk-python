"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#TagLogGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.log_group_name
    import aws_sdk_cloudwatch_logs.types.tags


class TagLogGroupRequest(TypedDict):
    log_group_name: "aws_sdk_cloudwatch_logs.types.log_group_name.LogGroupName"
    """<p>The name of the log group.</p>"""
    tags: "aws_sdk_cloudwatch_logs.types.tags.Tags"
    """<p>The key-value pairs to use for the tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagLogGroupRequest) -> dict:
    out: dict = {}
    out["logGroupName"] = value["log_group_name"]
    import aws_sdk_cloudwatch_logs.types.tags

    out["tags"] = aws_sdk_cloudwatch_logs.types.tags.serialize_aws_json_1_1(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagLogGroupRequest:
    out: TagLogGroupRequest = {}  # type: ignore[typeddict-item]
    if "logGroupName" in data:
        out["log_group_name"] = data["logGroupName"]
    else:
        raise DeserializationError("TagLogGroupRequest.log_group_name required")
    if "tags" in data:
        import aws_sdk_cloudwatch_logs.types.tags

        out["tags"] = aws_sdk_cloudwatch_logs.types.tags.deserialize_aws_json_1_1(
            data["tags"]
        )
    else:
        raise DeserializationError("TagLogGroupRequest.tags required")
    return out
