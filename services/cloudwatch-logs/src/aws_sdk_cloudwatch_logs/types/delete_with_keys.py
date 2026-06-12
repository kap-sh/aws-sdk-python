"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeleteWithKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.with_key

DeleteWithKeys: TypeAlias = list["aws_sdk_cloudwatch_logs.types.with_key.WithKey"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteWithKeys) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DeleteWithKeys:
    return list(data)
