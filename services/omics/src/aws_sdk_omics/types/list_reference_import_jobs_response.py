"""Generated from Smithy shape ``com.amazonaws.omics#ListReferenceImportJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_omics.types.import_reference_job_list
    import aws_sdk_omics.types.next_token


class ListReferenceImportJobsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_omics.types.next_token.NextToken"]
    """<p>A pagination token that's included if more results are available.</p>"""
    import_jobs: NotRequired[
        "aws_sdk_omics.types.import_reference_job_list.ImportReferenceJobList"
    ]
    """<p>A lis of jobs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReferenceImportJobsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "import_jobs" in value:
        import aws_sdk_omics.types.import_reference_job_list

        out["importJobs"] = (
            aws_sdk_omics.types.import_reference_job_list.serialize_json(
                value["import_jobs"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListReferenceImportJobsResponse:
    out: ListReferenceImportJobsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "importJobs" in data:
        import aws_sdk_omics.types.import_reference_job_list

        out["import_jobs"] = (
            aws_sdk_omics.types.import_reference_job_list.deserialize_json(
                data["importJobs"]
            )
        )
    return out
