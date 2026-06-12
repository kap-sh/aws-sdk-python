"""Generated from Smithy shape ``com.amazonaws.ecr#DescribePullThroughCacheRulesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecr.types.next_token
    import aws_sdk_ecr.types.pull_through_cache_rule_list


class DescribePullThroughCacheRulesResponse(TypedDict):
    pull_through_cache_rules: NotRequired[
        "aws_sdk_ecr.types.pull_through_cache_rule_list.PullThroughCacheRuleList"
    ]
    """<p>The details of the pull through cache rules.</p>"""
    next_token: NotRequired["aws_sdk_ecr.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> value to include in a future <code>DescribePullThroughCacheRulesRequest</code> request. When the results of a <code>DescribePullThroughCacheRulesRequest</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePullThroughCacheRulesResponse) -> dict:
    out: dict = {}
    if "pull_through_cache_rules" in value:
        import aws_sdk_ecr.types.pull_through_cache_rule_list

        out["pullThroughCacheRules"] = (
            aws_sdk_ecr.types.pull_through_cache_rule_list.serialize_aws_json_1_1(
                value["pull_through_cache_rules"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePullThroughCacheRulesResponse:
    out: DescribePullThroughCacheRulesResponse = {}  # type: ignore[typeddict-item]
    if "pullThroughCacheRules" in data:
        import aws_sdk_ecr.types.pull_through_cache_rule_list

        out["pull_through_cache_rules"] = (
            aws_sdk_ecr.types.pull_through_cache_rule_list.deserialize_aws_json_1_1(
                data["pullThroughCacheRules"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
