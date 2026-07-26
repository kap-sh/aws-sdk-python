"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LogGroupIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.log_group_identifier

LogGroupIdentifiers: TypeAlias = list[
    "capo_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogGroupIdentifiers) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> LogGroupIdentifiers:
    return list(data)
