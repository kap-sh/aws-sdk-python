"""Generated from Smithy shape ``com.amazonaws.healthlake#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_healthlake.types.tag_list.TagList"]
    """<p>Returns a list of tags associated with a data store. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_healthlake.types.tag_list

        out["Tags"] = capo_healthlake.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_healthlake.types.tag_list

        out["tags"] = capo_healthlake.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
