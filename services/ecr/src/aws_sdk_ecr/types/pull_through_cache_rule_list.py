"""Generated from Smithy shape ``com.amazonaws.ecr#PullThroughCacheRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecr.types.pull_through_cache_rule

PullThroughCacheRuleList: TypeAlias = list[
    "aws_sdk_ecr.types.pull_through_cache_rule.PullThroughCacheRule"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PullThroughCacheRuleList) -> list:
    import aws_sdk_ecr.types.pull_through_cache_rule

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ecr.types.pull_through_cache_rule.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PullThroughCacheRuleList:
    import aws_sdk_ecr.types.pull_through_cache_rule

    out: PullThroughCacheRuleList = []
    for item in data:
        out.append(
            aws_sdk_ecr.types.pull_through_cache_rule.deserialize_aws_json_1_1(item)
        )
    return out
