"""Generated from Smithy shape ``com.amazonaws.batch#ListQuotaSharesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.integer
    import aws_sdk_batch.types.string


class ListQuotaSharesRequest(TypedDict):
    job_queue: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name or full Amazon Resource Name (ARN) of the job queue used to list quota shares.</p>"""
    max_results: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>The maximum number of results returned by <code>ListQuotaShares</code> in paginated output. When this parameter is used, <code>ListQuotaShares</code> only returns <code>maxResults</code> results in a single page and a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListQuotaShares</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, <code>ListQuotaShares</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>"""
    next_token: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The <code>nextToken</code> value that's returned from a previous paginated <code>ListQuotaShares</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is <code>null</code> when there are no more results to return.</p> <note> <p>Treat this token as an opaque identifier that's only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListQuotaSharesRequest) -> dict:
    out: dict = {}
    if "job_queue" in value:
        out["jobQueue"] = value["job_queue"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListQuotaSharesRequest:
    out: ListQuotaSharesRequest = {}  # type: ignore[typeddict-item]
    if "jobQueue" in data:
        out["job_queue"] = data["jobQueue"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
