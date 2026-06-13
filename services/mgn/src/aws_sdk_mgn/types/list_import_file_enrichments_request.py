"""Generated from Smithy shape ``com.amazonaws.mgn#ListImportFileEnrichmentsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mgn.types.list_import_file_enrichments_filters
    import aws_sdk_mgn.types.max_results_type
    import aws_sdk_mgn.types.pagination_token


class ListImportFileEnrichmentsRequest(TypedDict):
    filters: NotRequired[
        "aws_sdk_mgn.types.list_import_file_enrichments_filters.ListImportFileEnrichmentsFilters"
    ]
    """<p>Filters to apply when listing import file enrichment jobs.</p>"""
    max_results: NotRequired["aws_sdk_mgn.types.max_results_type.MaxResultsType"]
    """<p>The maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["aws_sdk_mgn.types.pagination_token.PaginationToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImportFileEnrichmentsRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_mgn.types.list_import_file_enrichments_filters

        out["filters"] = (
            aws_sdk_mgn.types.list_import_file_enrichments_filters.serialize_json(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListImportFileEnrichmentsRequest:
    out: ListImportFileEnrichmentsRequest = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import aws_sdk_mgn.types.list_import_file_enrichments_filters

        out["filters"] = (
            aws_sdk_mgn.types.list_import_file_enrichments_filters.deserialize_json(
                data["filters"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
