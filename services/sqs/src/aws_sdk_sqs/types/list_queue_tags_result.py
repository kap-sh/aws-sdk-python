"""Generated from Smithy shape ``com.amazonaws.sqs#ListQueueTagsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sqs.types.tag_map


class ListQueueTagsResult(TypedDict):
    tags: NotRequired["aws_sdk_sqs.types.tag_map.TagMap"]
    """<p>The list of all tags added to the specified queue.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListQueueTagsResult) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_sqs.types.tag_map

        out["Tags"] = aws_sdk_sqs.types.tag_map.serialize_aws_json_1_0(value["tags"])
    return out


def deserialize_aws_json_1_0(data: dict) -> ListQueueTagsResult:
    out: ListQueueTagsResult = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_sqs.types.tag_map

        out["tags"] = aws_sdk_sqs.types.tag_map.deserialize_aws_json_1_0(data["Tags"])
    return out
