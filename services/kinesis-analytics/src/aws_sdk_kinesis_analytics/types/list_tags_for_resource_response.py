"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.tags


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["aws_sdk_kinesis_analytics.types.tags.Tags"]
    """<p>The key-value tags assigned to the application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_kinesis_analytics.types.tags

        out["Tags"] = aws_sdk_kinesis_analytics.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_kinesis_analytics.types.tags

        out["tags"] = aws_sdk_kinesis_analytics.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
