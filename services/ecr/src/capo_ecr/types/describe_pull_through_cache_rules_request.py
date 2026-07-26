"""Generated from Smithy shape ``com.amazonaws.ecr#DescribePullThroughCacheRulesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.max_results
    import capo_ecr.types.next_token
    import capo_ecr.types.pull_through_cache_rule_repository_prefix_list
    import capo_ecr.types.registry_id


class DescribePullThroughCacheRulesRequest(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry to return the pull through cache rules for. If you do not specify a registry, the default registry is assumed.</p>"""
    ecr_repository_prefixes: NotRequired[
        "capo_ecr.types.pull_through_cache_rule_repository_prefix_list.PullThroughCacheRuleRepositoryPrefixList"
    ]
    """<p>The Amazon ECR repository prefixes associated with the pull through cache rules to return. If no repository prefix value is specified, all pull through cache rules are returned.</p>"""
    next_token: NotRequired["capo_ecr.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> value returned from a previous paginated <code>DescribePullThroughCacheRulesRequest</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is null when there are no more results to return.</p>"""
    max_results: NotRequired["capo_ecr.types.max_results.MaxResults"]
    """<p>The maximum number of pull through cache rules returned by <code>DescribePullThroughCacheRulesRequest</code> in paginated output. When this parameter is used, <code>DescribePullThroughCacheRulesRequest</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>DescribePullThroughCacheRulesRequest</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 1000. If this parameter is not used, then <code>DescribePullThroughCacheRulesRequest</code> returns up to 100 results and a <code>nextToken</code> value, if applicable.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePullThroughCacheRulesRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "ecr_repository_prefixes" in value:
        import capo_ecr.types.pull_through_cache_rule_repository_prefix_list

        out["ecrRepositoryPrefixes"] = (
            capo_ecr.types.pull_through_cache_rule_repository_prefix_list.serialize_aws_json_1_1(
                value["ecr_repository_prefixes"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePullThroughCacheRulesRequest:
    out: DescribePullThroughCacheRulesRequest = {}  # type: ignore[typeddict-item]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "ecrRepositoryPrefixes" in data:
        import capo_ecr.types.pull_through_cache_rule_repository_prefix_list

        out["ecr_repository_prefixes"] = (
            capo_ecr.types.pull_through_cache_rule_repository_prefix_list.deserialize_aws_json_1_1(
                data["ecrRepositoryPrefixes"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
