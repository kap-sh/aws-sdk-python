"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#IndexPolicies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.index_policy

IndexPolicies: TypeAlias = list["capo_cloudwatch_logs.types.index_policy.IndexPolicy"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IndexPolicies) -> list:
    import capo_cloudwatch_logs.types.index_policy

    out: list = []
    for item in value:
        out.append(capo_cloudwatch_logs.types.index_policy.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> IndexPolicies:
    import capo_cloudwatch_logs.types.index_policy

    out: IndexPolicies = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch_logs.types.index_policy.deserialize_aws_json_1_1(item)
        )
    return out
