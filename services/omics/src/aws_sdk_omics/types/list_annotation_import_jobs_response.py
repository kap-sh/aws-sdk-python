"""Generated from Smithy shape ``com.amazonaws.omics#ListAnnotationImportJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_omics.types.annotation_import_job_items


class ListAnnotationImportJobsResponse(TypedDict):
    annotation_import_jobs: NotRequired[
        "aws_sdk_omics.types.annotation_import_job_items.AnnotationImportJobItems"
    ]
    """<p>A list of jobs.</p>"""
    next_token: NotRequired["str"]
    """<p>Specifies the pagination token from a previous request to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAnnotationImportJobsResponse) -> dict:
    out: dict = {}
    if "annotation_import_jobs" in value:
        import aws_sdk_omics.types.annotation_import_job_items

        out["annotationImportJobs"] = (
            aws_sdk_omics.types.annotation_import_job_items.serialize_json(
                value["annotation_import_jobs"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAnnotationImportJobsResponse:
    out: ListAnnotationImportJobsResponse = {}  # type: ignore[typeddict-item]
    if "annotationImportJobs" in data:
        import aws_sdk_omics.types.annotation_import_job_items

        out["annotation_import_jobs"] = (
            aws_sdk_omics.types.annotation_import_job_items.deserialize_json(
                data["annotationImportJobs"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
