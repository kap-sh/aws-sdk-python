"""Generated from Smithy shape ``com.amazonaws.ecrpublic#DescribeRegistriesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr_public.types.max_results
    import capo_ecr_public.types.next_token


class DescribeRegistriesRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_ecr_public.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> value that's returned from a previous paginated <code>DescribeRegistries</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. If there are no more results to return, this value is <code>null</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""
    max_results: NotRequired["capo_ecr_public.types.max_results.MaxResults"]
    """<p>The maximum number of repository results that's returned by <code>DescribeRegistries</code> in paginated output. When this parameter is used, <code>DescribeRegistries</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>DescribeRegistries</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 1000. If this parameter isn't used, then <code>DescribeRegistries</code> returns up to 100 results and a <code>nextToken</code> value, if applicable.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRegistriesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRegistriesRequest:
    out: DescribeRegistriesRequest = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
