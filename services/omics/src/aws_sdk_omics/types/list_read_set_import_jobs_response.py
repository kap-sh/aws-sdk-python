"""Generated from Smithy shape ``com.amazonaws.omics#ListReadSetImportJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.import_read_set_job_list
    import aws_sdk_omics.types.next_token


class ListReadSetImportJobsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_omics.types.next_token.NextToken"]
    """<p>A pagination token that's included if more results are available.</p>"""
    import_jobs: NotRequired[
        "aws_sdk_omics.types.import_read_set_job_list.ImportReadSetJobList"
    ]
    """<p>A list of jobs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReadSetImportJobsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "import_jobs" in value:
        import aws_sdk_omics.types.import_read_set_job_list

        out["importJobs"] = aws_sdk_omics.types.import_read_set_job_list.serialize_json(
            value["import_jobs"]
        )
    return out


def deserialize_json(data: dict) -> ListReadSetImportJobsResponse:
    out: ListReadSetImportJobsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "importJobs" in data:
        import aws_sdk_omics.types.import_read_set_job_list

        out["import_jobs"] = (
            aws_sdk_omics.types.import_read_set_job_list.deserialize_json(
                data["importJobs"]
            )
        )
    return out
