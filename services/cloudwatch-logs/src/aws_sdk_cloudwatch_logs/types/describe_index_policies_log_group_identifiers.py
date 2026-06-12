"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeIndexPoliciesLogGroupIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.log_group_identifier

DescribeIndexPoliciesLogGroupIdentifiers: TypeAlias = list[
    "aws_sdk_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeIndexPoliciesLogGroupIdentifiers) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DescribeIndexPoliciesLogGroupIdentifiers:
    return list(data)
