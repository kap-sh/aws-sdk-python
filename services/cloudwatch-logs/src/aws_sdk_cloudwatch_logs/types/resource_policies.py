"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ResourcePolicies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.resource_policy

ResourcePolicies: TypeAlias = list[
    "aws_sdk_cloudwatch_logs.types.resource_policy.ResourcePolicy"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourcePolicies) -> list:
    import aws_sdk_cloudwatch_logs.types.resource_policy

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch_logs.types.resource_policy.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResourcePolicies:
    import aws_sdk_cloudwatch_logs.types.resource_policy

    out: ResourcePolicies = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_logs.types.resource_policy.deserialize_aws_json_1_1(item)
        )
    return out
