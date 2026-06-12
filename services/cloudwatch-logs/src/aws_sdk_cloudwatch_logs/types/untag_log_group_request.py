"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#UntagLogGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.log_group_name
    import aws_sdk_cloudwatch_logs.types.tag_list


class UntagLogGroupRequest(TypedDict):
    log_group_name: "aws_sdk_cloudwatch_logs.types.log_group_name.LogGroupName"
    """<p>The name of the log group.</p>"""
    tags: "aws_sdk_cloudwatch_logs.types.tag_list.TagList"
    """<p>The tag keys. The corresponding tags are removed from the log group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagLogGroupRequest) -> dict:
    out: dict = {}
    out["logGroupName"] = value["log_group_name"]
    import aws_sdk_cloudwatch_logs.types.tag_list

    out["tags"] = aws_sdk_cloudwatch_logs.types.tag_list.serialize_aws_json_1_1(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagLogGroupRequest:
    out: UntagLogGroupRequest = {}  # type: ignore[typeddict-item]
    if "logGroupName" in data:
        out["log_group_name"] = data["logGroupName"]
    else:
        raise DeserializationError("UntagLogGroupRequest.log_group_name required")
    if "tags" in data:
        import aws_sdk_cloudwatch_logs.types.tag_list

        out["tags"] = aws_sdk_cloudwatch_logs.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    else:
        raise DeserializationError("UntagLogGroupRequest.tags required")
    return out
