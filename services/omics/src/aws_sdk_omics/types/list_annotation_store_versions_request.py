"""Generated from Smithy shape ``com.amazonaws.omics#ListAnnotationStoreVersionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_omics.types.list_annotation_store_versions_filter


class ListAnnotationStoreVersionsRequest(TypedDict):
    name: "str"
    """<p> The name of an annotation store. </p>"""
    max_results: NotRequired["int"]
    """<p> The maximum number of annotation store versions to return in one page of results. </p>"""
    next_token: NotRequired["str"]
    """<p> Specifies the pagination token from a previous request to retrieve the next page of results. </p>"""
    filter: NotRequired[
        "aws_sdk_omics.types.list_annotation_store_versions_filter.ListAnnotationStoreVersionsFilter"
    ]
    """<p> A filter to apply to the list of annotation store versions. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAnnotationStoreVersionsRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import aws_sdk_omics.types.list_annotation_store_versions_filter

        out["filter"] = (
            aws_sdk_omics.types.list_annotation_store_versions_filter.serialize_json(
                value["filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListAnnotationStoreVersionsRequest:
    out: ListAnnotationStoreVersionsRequest = {}  # type: ignore[typeddict-item]
    if "filter" in data:
        import aws_sdk_omics.types.list_annotation_store_versions_filter

        out["filter"] = (
            aws_sdk_omics.types.list_annotation_store_versions_filter.deserialize_json(
                data["filter"]
            )
        )
    return out
