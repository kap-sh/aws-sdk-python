"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LowerCaseStringWithKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.with_key

LowerCaseStringWithKeys: TypeAlias = list[
    "aws_sdk_cloudwatch_logs.types.with_key.WithKey"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LowerCaseStringWithKeys) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> LowerCaseStringWithKeys:
    return list(data)
