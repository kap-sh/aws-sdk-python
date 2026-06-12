"""Generated from Smithy shape ``com.amazonaws.marketplacedeployment#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_marketplace_deployment.types.tags

class ListTagsForResourceResponse(TypedDict):
    tags: NotRequired["aws_sdk_marketplace_deployment.types.tags.Tags"]
    """<p>A map of key-value pairs, where each pair represents a tag present on the resource.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_marketplace_deployment.types.tags
        out["tags"] = aws_sdk_marketplace_deployment.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_marketplace_deployment.types.tags
        out["tags"] = aws_sdk_marketplace_deployment.types.tags.deserialize_json(data["tags"])
    return out