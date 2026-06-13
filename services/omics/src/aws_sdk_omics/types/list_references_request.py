"""Generated from Smithy shape ``com.amazonaws.omics#ListReferencesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_omics.types.next_token
    import aws_sdk_omics.types.reference_filter
    import aws_sdk_omics.types.reference_store_id


class ListReferencesRequest(TypedDict):
    reference_store_id: "aws_sdk_omics.types.reference_store_id.ReferenceStoreId"
    """<p>The references' reference store ID.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of references to return in one page of results.</p>"""
    next_token: NotRequired["aws_sdk_omics.types.next_token.NextToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""
    filter: NotRequired["aws_sdk_omics.types.reference_filter.ReferenceFilter"]
    """<p>A filter to apply to the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReferencesRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import aws_sdk_omics.types.reference_filter

        out["filter"] = aws_sdk_omics.types.reference_filter.serialize_json(
            value["filter"]
        )
    return out


def deserialize_json(data: dict) -> ListReferencesRequest:
    out: ListReferencesRequest = {}  # type: ignore[typeddict-item]
    if "filter" in data:
        import aws_sdk_omics.types.reference_filter

        out["filter"] = aws_sdk_omics.types.reference_filter.deserialize_json(
            data["filter"]
        )
    return out
