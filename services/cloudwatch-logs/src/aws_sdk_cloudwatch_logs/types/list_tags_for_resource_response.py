"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.tags


class ListTagsForResourceResponse(TypedDict):
    tags: NotRequired["aws_sdk_cloudwatch_logs.types.tags.Tags"]
    """<p>The list of tags associated with the requested resource.></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_cloudwatch_logs.types.tags

        out["tags"] = aws_sdk_cloudwatch_logs.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_cloudwatch_logs.types.tags

        out["tags"] = aws_sdk_cloudwatch_logs.types.tags.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
