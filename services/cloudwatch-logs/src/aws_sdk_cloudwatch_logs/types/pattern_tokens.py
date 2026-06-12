"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PatternTokens``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.pattern_token

PatternTokens: TypeAlias = list[
    "aws_sdk_cloudwatch_logs.types.pattern_token.PatternToken"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatternTokens) -> list:
    import aws_sdk_cloudwatch_logs.types.pattern_token

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch_logs.types.pattern_token.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PatternTokens:
    import aws_sdk_cloudwatch_logs.types.pattern_token

    out: PatternTokens = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_logs.types.pattern_token.deserialize_aws_json_1_1(item)
        )
    return out
