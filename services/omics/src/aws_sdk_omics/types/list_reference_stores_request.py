"""Generated from Smithy shape ``com.amazonaws.omics#ListReferenceStoresRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_omics.types.next_token
    import aws_sdk_omics.types.reference_store_filter


class ListReferenceStoresRequest(TypedDict):
    max_results: NotRequired["int"]
    """<p>The maximum number of stores to return in one page of results.</p>"""
    next_token: NotRequired["aws_sdk_omics.types.next_token.NextToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""
    filter: NotRequired[
        "aws_sdk_omics.types.reference_store_filter.ReferenceStoreFilter"
    ]
    """<p>A filter to apply to the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReferenceStoresRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import aws_sdk_omics.types.reference_store_filter

        out["filter"] = aws_sdk_omics.types.reference_store_filter.serialize_json(
            value["filter"]
        )
    return out


def deserialize_json(data: dict) -> ListReferenceStoresRequest:
    out: ListReferenceStoresRequest = {}  # type: ignore[typeddict-item]
    if "filter" in data:
        import aws_sdk_omics.types.reference_store_filter

        out["filter"] = aws_sdk_omics.types.reference_store_filter.deserialize_json(
            data["filter"]
        )
    return out
