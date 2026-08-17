"""Generated from Smithy shape ``com.amazonaws.sqs#ListQueueTagsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sqs.types.tag_map


class ListQueueTagsResult(TypedDict, closed=True):
    tags: NotRequired["capo_sqs.types.tag_map.TagMap"]
    """<p>The list of all tags added to the specified queue.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListQueueTagsResult) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_sqs.types.tag_map

        out["Tags"] = capo_sqs.types.tag_map.serialize_aws_json_1_0(value["tags"])
    return out


def deserialize_aws_json_1_0(data: dict) -> ListQueueTagsResult:
    out: ListQueueTagsResult = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_sqs.types.tag_map

        out["tags"] = capo_sqs.types.tag_map.deserialize_aws_json_1_0(data["Tags"])
    return out
