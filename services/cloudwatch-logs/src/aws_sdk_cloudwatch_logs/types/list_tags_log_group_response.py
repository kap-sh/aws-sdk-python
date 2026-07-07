"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ListTagsLogGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.tags


class ListTagsLogGroupResponse(TypedDict, closed=True):
    tags: NotRequired["aws_sdk_cloudwatch_logs.types.tags.Tags"]
    """<p>The tags for the log group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsLogGroupResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_cloudwatch_logs.types.tags

        out["tags"] = aws_sdk_cloudwatch_logs.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsLogGroupResponse:
    out: ListTagsLogGroupResponse = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_cloudwatch_logs.types.tags

        out["tags"] = aws_sdk_cloudwatch_logs.types.tags.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
