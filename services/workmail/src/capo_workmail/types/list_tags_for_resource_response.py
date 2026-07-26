"""Generated from Smithy shape ``com.amazonaws.workmail#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_workmail.types.tag_list.TagList"]
    """<p>A list of tag key-value pairs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_workmail.types.tag_list

        out["Tags"] = capo_workmail.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_workmail.types.tag_list

        out["tags"] = capo_workmail.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
