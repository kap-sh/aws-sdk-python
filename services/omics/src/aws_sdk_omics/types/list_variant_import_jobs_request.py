"""Generated from Smithy shape ``com.amazonaws.omics#ListVariantImportJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.id_list
    import aws_sdk_omics.types.list_variant_import_jobs_filter


class ListVariantImportJobsRequest(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of import jobs to return in one page of results.</p>"""
    ids: NotRequired["aws_sdk_omics.types.id_list.IdList"]
    """<p>A list of job IDs.</p>"""
    next_token: NotRequired["str"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""
    filter: NotRequired[
        "aws_sdk_omics.types.list_variant_import_jobs_filter.ListVariantImportJobsFilter"
    ]
    """<p>A filter to apply to the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVariantImportJobsRequest) -> dict:
    out: dict = {}
    if "ids" in value:
        import aws_sdk_omics.types.id_list

        out["ids"] = aws_sdk_omics.types.id_list.serialize_json(value["ids"])
    if "filter" in value:
        import aws_sdk_omics.types.list_variant_import_jobs_filter

        out["filter"] = (
            aws_sdk_omics.types.list_variant_import_jobs_filter.serialize_json(
                value["filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListVariantImportJobsRequest:
    out: ListVariantImportJobsRequest = {}  # type: ignore[typeddict-item]
    if "ids" in data:
        import aws_sdk_omics.types.id_list

        out["ids"] = aws_sdk_omics.types.id_list.deserialize_json(data["ids"])
    if "filter" in data:
        import aws_sdk_omics.types.list_variant_import_jobs_filter

        out["filter"] = (
            aws_sdk_omics.types.list_variant_import_jobs_filter.deserialize_json(
                data["filter"]
            )
        )
    return out
