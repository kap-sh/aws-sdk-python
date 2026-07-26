"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ResourcePolicies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.resource_policy

ResourcePolicies: TypeAlias = list[
    "capo_cloudwatch_logs.types.resource_policy.ResourcePolicy"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourcePolicies) -> list:
    import capo_cloudwatch_logs.types.resource_policy

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch_logs.types.resource_policy.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResourcePolicies:
    import capo_cloudwatch_logs.types.resource_policy

    out: ResourcePolicies = []
    for item in data:
        out.append(
            capo_cloudwatch_logs.types.resource_policy.deserialize_aws_json_1_1(item)
        )
    return out
