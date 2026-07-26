"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pca_connector_scep.types.tags


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_pca_connector_scep.types.tags.Tags"]
    """<p>The key-value pairs to associate with the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_pca_connector_scep.types.tags

        out["Tags"] = capo_pca_connector_scep.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_pca_connector_scep.types.tags

        out["tags"] = capo_pca_connector_scep.types.tags.deserialize_json(data["Tags"])
    return out
