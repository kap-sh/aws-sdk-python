"""Generated from Smithy shape ``com.amazonaws.batch#DescribeJobQueuesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.integer
    import capo_batch.types.string
    import capo_batch.types.string_list


class DescribeJobQueuesRequest(TypedDict, closed=True):
    job_queues: NotRequired["capo_batch.types.string_list.StringList"]
    """<p>A list of up to 100 queue names or full queue Amazon Resource Name (ARN) entries.</p>"""
    max_results: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The maximum number of results returned by <code>DescribeJobQueues</code> in paginated output. When this parameter is used, <code>DescribeJobQueues</code> only returns <code>maxResults</code> results in a single page and a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>DescribeJobQueues</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>DescribeJobQueues</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>"""
    next_token: NotRequired["capo_batch.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a previous paginated <code>DescribeJobQueues</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is <code>null</code> when there are no more results to return.</p> <note> <p>Treat this token as an opaque identifier that's only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobQueuesRequest) -> dict:
    out: dict = {}
    if "job_queues" in value:
        import capo_batch.types.string_list

        out["jobQueues"] = capo_batch.types.string_list.serialize_json(
            value["job_queues"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeJobQueuesRequest:
    out: DescribeJobQueuesRequest = {}  # type: ignore[typeddict-item]
    if "jobQueues" in data:
        import capo_batch.types.string_list

        out["job_queues"] = capo_batch.types.string_list.deserialize_json(
            data["jobQueues"]
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
