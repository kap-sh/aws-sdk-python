"""Generated from Smithy shape ``com.amazonaws.opensearch#ListTagsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.tag_list


class ListTagsResponse(TypedDict, closed=True):
    tag_list: NotRequired["capo_opensearch.types.tag_list.TagList"]
    """<p>List of resource tags associated with the specified domain, data source, or application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsResponse) -> dict:
    out: dict = {}
    if "tag_list" in value:
        import capo_opensearch.types.tag_list

        out["TagList"] = capo_opensearch.types.tag_list.serialize_json(
            value["tag_list"]
        )
    return out


def deserialize_json(data: dict) -> ListTagsResponse:
    out: ListTagsResponse = {}  # type: ignore[typeddict-item]
    if "TagList" in data:
        import capo_opensearch.types.tag_list

        out["tag_list"] = capo_opensearch.types.tag_list.deserialize_json(
            data["TagList"]
        )
    return out
