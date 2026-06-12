"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#AccountPolicies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.account_policy

AccountPolicies: TypeAlias = list[
    "aws_sdk_cloudwatch_logs.types.account_policy.AccountPolicy"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountPolicies) -> list:
    import aws_sdk_cloudwatch_logs.types.account_policy

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch_logs.types.account_policy.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AccountPolicies:
    import aws_sdk_cloudwatch_logs.types.account_policy

    out: AccountPolicies = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_logs.types.account_policy.deserialize_aws_json_1_1(item)
        )
    return out
