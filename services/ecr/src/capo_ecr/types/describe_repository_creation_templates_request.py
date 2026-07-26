"""Generated from Smithy shape ``com.amazonaws.ecr#DescribeRepositoryCreationTemplatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.max_results
    import capo_ecr.types.next_token
    import capo_ecr.types.prefix_list


class DescribeRepositoryCreationTemplatesRequest(TypedDict, closed=True):
    prefixes: NotRequired["capo_ecr.types.prefix_list.PrefixList"]
    """<p>The repository namespace prefixes associated with the repository creation templates to describe. If this value is not specified, all repository creation templates are returned.</p>"""
    next_token: NotRequired["capo_ecr.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> value returned from a previous paginated <code>DescribeRepositoryCreationTemplates</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is <code>null</code> when there are no more results to return.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""
    max_results: NotRequired["capo_ecr.types.max_results.MaxResults"]
    """<p>The maximum number of repository results returned by <code>DescribeRepositoryCreationTemplatesRequest</code> in paginated output. When this parameter is used, <code>DescribeRepositoryCreationTemplatesRequest</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>DescribeRepositoryCreationTemplatesRequest</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 1000. If this parameter is not used, then <code>DescribeRepositoryCreationTemplatesRequest</code> returns up to 100 results and a <code>nextToken</code> value, if applicable.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRepositoryCreationTemplatesRequest) -> dict:
    out: dict = {}
    if "prefixes" in value:
        import capo_ecr.types.prefix_list

        out["prefixes"] = capo_ecr.types.prefix_list.serialize_aws_json_1_1(
            value["prefixes"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRepositoryCreationTemplatesRequest:
    out: DescribeRepositoryCreationTemplatesRequest = {}  # type: ignore[typeddict-item]
    if "prefixes" in data:
        import capo_ecr.types.prefix_list

        out["prefixes"] = capo_ecr.types.prefix_list.deserialize_aws_json_1_1(
            data["prefixes"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
