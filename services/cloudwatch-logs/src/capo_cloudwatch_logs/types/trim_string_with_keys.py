"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#TrimStringWithKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.with_key

TrimStringWithKeys: TypeAlias = list["capo_cloudwatch_logs.types.with_key.WithKey"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrimStringWithKeys) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TrimStringWithKeys:
    return [item for item in data if item is not None]
