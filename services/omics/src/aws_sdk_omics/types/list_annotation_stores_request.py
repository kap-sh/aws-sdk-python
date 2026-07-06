"""Generated from Smithy shape ``com.amazonaws.omics#ListAnnotationStoresRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.id_list
    import aws_sdk_omics.types.list_annotation_stores_filter


class ListAnnotationStoresRequest(TypedDict, closed=True):
    ids: NotRequired["aws_sdk_omics.types.id_list.IdList"]
    """<p>IDs of stores to list.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of stores to return in one page of results.</p>"""
    next_token: NotRequired["str"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""
    filter: NotRequired[
        "aws_sdk_omics.types.list_annotation_stores_filter.ListAnnotationStoresFilter"
    ]
    """<p>A filter to apply to the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAnnotationStoresRequest) -> dict:
    out: dict = {}
    if "ids" in value:
        import aws_sdk_omics.types.id_list

        out["ids"] = aws_sdk_omics.types.id_list.serialize_json(value["ids"])
    if "filter" in value:
        import aws_sdk_omics.types.list_annotation_stores_filter

        out["filter"] = (
            aws_sdk_omics.types.list_annotation_stores_filter.serialize_json(
                value["filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListAnnotationStoresRequest:
    out: ListAnnotationStoresRequest = {}  # type: ignore[typeddict-item]
    if "ids" in data:
        import aws_sdk_omics.types.id_list

        out["ids"] = aws_sdk_omics.types.id_list.deserialize_json(data["ids"])
    if "filter" in data:
        import aws_sdk_omics.types.list_annotation_stores_filter

        out["filter"] = (
            aws_sdk_omics.types.list_annotation_stores_filter.deserialize_json(
                data["filter"]
            )
        )
    return out
