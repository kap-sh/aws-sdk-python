"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeIndexPoliciesLogGroupIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.log_group_identifier

DescribeIndexPoliciesLogGroupIdentifiers: TypeAlias = list[
    "capo_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeIndexPoliciesLogGroupIdentifiers) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DescribeIndexPoliciesLogGroupIdentifiers:
    return [item for item in data if item is not None]
