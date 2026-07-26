"""Generated from Smithy shape ``com.amazonaws.omics#ListAnnotationStoresResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.annotation_store_items


class ListAnnotationStoresResponse(TypedDict, closed=True):
    annotation_stores: NotRequired[
        "capo_omics.types.annotation_store_items.AnnotationStoreItems"
    ]
    """<p>A list of stores.</p>"""
    next_token: NotRequired["str"]
    """<p>A pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAnnotationStoresResponse) -> dict:
    out: dict = {}
    if "annotation_stores" in value:
        import capo_omics.types.annotation_store_items

        out["annotationStores"] = (
            capo_omics.types.annotation_store_items.serialize_json(
                value["annotation_stores"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAnnotationStoresResponse:
    out: ListAnnotationStoresResponse = {}  # type: ignore[typeddict-item]
    if "annotationStores" in data:
        import capo_omics.types.annotation_store_items

        out["annotation_stores"] = (
            capo_omics.types.annotation_store_items.deserialize_json(
                data["annotationStores"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
