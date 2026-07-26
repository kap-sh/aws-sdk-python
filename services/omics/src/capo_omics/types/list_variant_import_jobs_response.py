"""Generated from Smithy shape ``com.amazonaws.omics#ListVariantImportJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.variant_import_job_items


class ListVariantImportJobsResponse(TypedDict, closed=True):
    variant_import_jobs: NotRequired[
        "capo_omics.types.variant_import_job_items.VariantImportJobItems"
    ]
    """<p>A list of jobs.</p>"""
    next_token: NotRequired["str"]
    """<p>A pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVariantImportJobsResponse) -> dict:
    out: dict = {}
    if "variant_import_jobs" in value:
        import capo_omics.types.variant_import_job_items

        out["variantImportJobs"] = (
            capo_omics.types.variant_import_job_items.serialize_json(
                value["variant_import_jobs"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListVariantImportJobsResponse:
    out: ListVariantImportJobsResponse = {}  # type: ignore[typeddict-item]
    if "variantImportJobs" in data:
        import capo_omics.types.variant_import_job_items

        out["variant_import_jobs"] = (
            capo_omics.types.variant_import_job_items.deserialize_json(
                data["variantImportJobs"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
