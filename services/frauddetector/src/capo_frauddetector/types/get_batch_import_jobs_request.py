"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetBatchImportJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.batch_imports_max_page_size
    import capo_frauddetector.types.identifier
    import capo_frauddetector.types.string


class GetBatchImportJobsRequest(TypedDict, closed=True):
    job_id: NotRequired["capo_frauddetector.types.identifier.identifier"]
    """<p>The ID of the batch import job to get.</p>"""
    max_results: NotRequired[
        "capo_frauddetector.types.batch_imports_max_page_size.batchImportsMaxPageSize"
    ]
    """<p>The maximum number of objects to return for request.</p>"""
    next_token: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The next token from the previous request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetBatchImportJobsRequest) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetBatchImportJobsRequest:
    out: GetBatchImportJobsRequest = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
