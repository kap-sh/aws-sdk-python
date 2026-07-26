"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.tags


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_opensearchserverless.types.tags.Tags"]
    """<p>The tags associated with the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_opensearchserverless.types.tags

        out["tags"] = capo_opensearchserverless.types.tags.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_opensearchserverless.types.tags

        out["tags"] = capo_opensearchserverless.types.tags.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
