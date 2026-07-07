"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pca_connector_ad.types.tags


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["aws_sdk_pca_connector_ad.types.tags.Tags"]
    """<p>The tags, if any, that are associated with your resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_pca_connector_ad.types.tags

        out["Tags"] = aws_sdk_pca_connector_ad.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_pca_connector_ad.types.tags

        out["tags"] = aws_sdk_pca_connector_ad.types.tags.deserialize_json(data["Tags"])
    return out
