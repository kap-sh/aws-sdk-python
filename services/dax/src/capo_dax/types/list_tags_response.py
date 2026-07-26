"""Generated from Smithy shape ``com.amazonaws.dax#ListTagsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dax.types.string
    import capo_dax.types.tag_list


class ListTagsResponse(TypedDict, closed=True):
    tags: NotRequired["capo_dax.types.tag_list.TagList"]
    """<p>A list of tags currently associated with the DAX cluster.</p>"""
    next_token: NotRequired["capo_dax.types.string.String"]
    """<p>If this value is present, there are additional results to be displayed. To retrieve them, call <code>ListTags</code> again, with <code>NextToken</code> set to this value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_dax.types.tag_list

        out["Tags"] = capo_dax.types.tag_list.serialize_aws_json_1_1(value["tags"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsResponse:
    out: ListTagsResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_dax.types.tag_list

        out["tags"] = capo_dax.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
