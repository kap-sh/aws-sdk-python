"""Generated from Smithy shape ``com.amazonaws.ecr#PullThroughCacheRuleRepositoryPrefixList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr.types.pull_through_cache_rule_repository_prefix

PullThroughCacheRuleRepositoryPrefixList: TypeAlias = list[
    "capo_ecr.types.pull_through_cache_rule_repository_prefix.PullThroughCacheRuleRepositoryPrefix"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PullThroughCacheRuleRepositoryPrefixList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PullThroughCacheRuleRepositoryPrefixList:
    return [item for item in data if item is not None]
