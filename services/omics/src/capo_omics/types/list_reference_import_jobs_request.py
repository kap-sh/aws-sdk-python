"""Generated from Smithy shape ``com.amazonaws.omics#ListReferenceImportJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.import_reference_filter
    import capo_omics.types.next_token
    import capo_omics.types.reference_store_id


class ListReferenceImportJobsRequest(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of jobs to return in one page of results.</p>"""
    next_token: NotRequired["capo_omics.types.next_token.NextToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""
    reference_store_id: "capo_omics.types.reference_store_id.ReferenceStoreId"
    """<p>The job's reference store ID.</p>"""
    filter: NotRequired[
        "capo_omics.types.import_reference_filter.ImportReferenceFilter"
    ]
    """<p>A filter to apply to the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReferenceImportJobsRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import capo_omics.types.import_reference_filter

        out["filter"] = capo_omics.types.import_reference_filter.serialize_json(
            value["filter"]
        )
    return out


def deserialize_json(data: dict) -> ListReferenceImportJobsRequest:
    out: ListReferenceImportJobsRequest = {}  # type: ignore[typeddict-item]
    if "filter" in data:
        import capo_omics.types.import_reference_filter

        out["filter"] = capo_omics.types.import_reference_filter.deserialize_json(
            data["filter"]
        )
    return out
