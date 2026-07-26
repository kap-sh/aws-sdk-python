"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog_appregistry.types.tags


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_service_catalog_appregistry.types.tags.Tags"]
    """<p>The tags on the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_service_catalog_appregistry.types.tags

        out["tags"] = capo_service_catalog_appregistry.types.tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_service_catalog_appregistry.types.tags

        out["tags"] = capo_service_catalog_appregistry.types.tags.deserialize_json(
            data["tags"]
        )
    return out
