"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.tags


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_cloudwatch_logs.types.tags.Tags"]
    """<p>The list of tags associated with the requested resource.></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_cloudwatch_logs.types.tags

        out["tags"] = capo_cloudwatch_logs.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_cloudwatch_logs.types.tags

        out["tags"] = capo_cloudwatch_logs.types.tags.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
