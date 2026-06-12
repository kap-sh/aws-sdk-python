"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#MatchPatterns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.match_pattern

MatchPatterns: TypeAlias = list[
    "aws_sdk_cloudwatch_logs.types.match_pattern.MatchPattern"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MatchPatterns) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> MatchPatterns:
    return list(data)
