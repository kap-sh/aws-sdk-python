"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ReplayDestinationFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.arn

ReplayDestinationFilters: TypeAlias = list["aws_sdk_cloudwatch_events.types.arn.Arn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplayDestinationFilters) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ReplayDestinationFilters:
    return list(data)
