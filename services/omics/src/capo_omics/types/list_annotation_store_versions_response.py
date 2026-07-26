"""Generated from Smithy shape ``com.amazonaws.omics#ListAnnotationStoreVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.annotation_store_version_items


class ListAnnotationStoreVersionsResponse(TypedDict, closed=True):
    annotation_store_versions: NotRequired[
        "capo_omics.types.annotation_store_version_items.AnnotationStoreVersionItems"
    ]
    """<p> Lists all versions of an annotation store. </p>"""
    next_token: NotRequired["str"]
    """<p> Specifies the pagination token from a previous request to retrieve the next page of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAnnotationStoreVersionsResponse) -> dict:
    out: dict = {}
    if "annotation_store_versions" in value:
        import capo_omics.types.annotation_store_version_items

        out["annotationStoreVersions"] = (
            capo_omics.types.annotation_store_version_items.serialize_json(
                value["annotation_store_versions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAnnotationStoreVersionsResponse:
    out: ListAnnotationStoreVersionsResponse = {}  # type: ignore[typeddict-item]
    if "annotationStoreVersions" in data:
        import capo_omics.types.annotation_store_version_items

        out["annotation_store_versions"] = (
            capo_omics.types.annotation_store_version_items.deserialize_json(
                data["annotationStoreVersions"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
