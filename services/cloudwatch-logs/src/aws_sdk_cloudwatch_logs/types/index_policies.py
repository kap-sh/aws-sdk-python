"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#IndexPolicies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.index_policy

IndexPolicies: TypeAlias = list[
    "aws_sdk_cloudwatch_logs.types.index_policy.IndexPolicy"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IndexPolicies) -> list:
    import aws_sdk_cloudwatch_logs.types.index_policy

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch_logs.types.index_policy.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> IndexPolicies:
    import aws_sdk_cloudwatch_logs.types.index_policy

    out: IndexPolicies = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_logs.types.index_policy.deserialize_aws_json_1_1(item)
        )
    return out
