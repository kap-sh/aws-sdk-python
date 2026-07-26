"""Generated from Smithy shape ``com.amazonaws.batch#DescribeComputeEnvironmentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.integer
    import capo_batch.types.string
    import capo_batch.types.string_list


class DescribeComputeEnvironmentsRequest(TypedDict, closed=True):
    compute_environments: NotRequired["capo_batch.types.string_list.StringList"]
    """<p>A list of up to 100 compute environment names or full Amazon Resource Name (ARN) entries.</p>"""
    max_results: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The maximum number of cluster results returned by <code>DescribeComputeEnvironments</code> in paginated output. When this parameter is used, <code>DescribeComputeEnvironments</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>DescribeComputeEnvironments</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>DescribeComputeEnvironments</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>"""
    next_token: NotRequired["capo_batch.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a previous paginated <code>DescribeComputeEnvironments</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is <code>null</code> when there are no more results to return.</p> <note> <p>Treat this token as an opaque identifier that's only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeComputeEnvironmentsRequest) -> dict:
    out: dict = {}
    if "compute_environments" in value:
        import capo_batch.types.string_list

        out["computeEnvironments"] = capo_batch.types.string_list.serialize_json(
            value["compute_environments"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeComputeEnvironmentsRequest:
    out: DescribeComputeEnvironmentsRequest = {}  # type: ignore[typeddict-item]
    if "computeEnvironments" in data:
        import capo_batch.types.string_list

        out["compute_environments"] = capo_batch.types.string_list.deserialize_json(
            data["computeEnvironments"]
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
