"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ListTagsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.tag_list


class ListTagsResponse(TypedDict):
    tag_list: NotRequired["aws_sdk_elasticsearch_service.types.tag_list.TagList"]
    """<p> List of <code>Tag</code> for the requested Elasticsearch domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsResponse) -> dict:
    out: dict = {}
    if "tag_list" in value:
        import aws_sdk_elasticsearch_service.types.tag_list

        out["TagList"] = aws_sdk_elasticsearch_service.types.tag_list.serialize_json(
            value["tag_list"]
        )
    return out


def deserialize_json(data: dict) -> ListTagsResponse:
    out: ListTagsResponse = {}  # type: ignore[typeddict-item]
    if "TagList" in data:
        import aws_sdk_elasticsearch_service.types.tag_list

        out["tag_list"] = aws_sdk_elasticsearch_service.types.tag_list.deserialize_json(
            data["TagList"]
        )
    return out
