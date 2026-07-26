"""Generated from Smithy shape ``com.amazonaws.ecrpublic#DescribeRepositoriesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr_public.types.max_results
    import capo_ecr_public.types.next_token
    import capo_ecr_public.types.registry_id
    import capo_ecr_public.types.repository_name_list


class DescribeRepositoriesRequest(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr_public.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID that's associated with the registry that contains the repositories to be described. If you do not specify a registry, the default public registry is assumed.</p>"""
    repository_names: NotRequired[
        "capo_ecr_public.types.repository_name_list.RepositoryNameList"
    ]
    """<p>A list of repositories to describe. If this parameter is omitted, then all repositories in a registry are described.</p>"""
    next_token: NotRequired["capo_ecr_public.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> value that's returned from a previous paginated <code>DescribeRepositories</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. If there are no more results to return, this value is <code>null</code>. If you specify repositories with <code>repositoryNames</code>, you can't use this option.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""
    max_results: NotRequired["capo_ecr_public.types.max_results.MaxResults"]
    """<p>The maximum number of repository results that's returned by <code>DescribeRepositories</code> in paginated output. When this parameter is used, <code>DescribeRepositories</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>DescribeRepositories</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 1000. If this parameter isn't used, then <code>DescribeRepositories</code> returns up to 100 results and a <code>nextToken</code> value, if applicable. If you specify repositories with <code>repositoryNames</code>, you can't use this option.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRepositoriesRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "repository_names" in value:
        import capo_ecr_public.types.repository_name_list

        out["repositoryNames"] = (
            capo_ecr_public.types.repository_name_list.serialize_aws_json_1_1(
                value["repository_names"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRepositoriesRequest:
    out: DescribeRepositoriesRequest = {}  # type: ignore[typeddict-item]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "repositoryNames" in data:
        import capo_ecr_public.types.repository_name_list

        out["repository_names"] = (
            capo_ecr_public.types.repository_name_list.deserialize_aws_json_1_1(
                data["repositoryNames"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
