"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ScheduledQueryDestinationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.scheduled_query_destination

ScheduledQueryDestinationList: TypeAlias = list[
    "aws_sdk_cloudwatch_logs.types.scheduled_query_destination.ScheduledQueryDestination"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScheduledQueryDestinationList) -> list:
    import aws_sdk_cloudwatch_logs.types.scheduled_query_destination

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch_logs.types.scheduled_query_destination.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ScheduledQueryDestinationList:
    import aws_sdk_cloudwatch_logs.types.scheduled_query_destination

    out: ScheduledQueryDestinationList = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_logs.types.scheduled_query_destination.deserialize_aws_json_1_1(
                item
            )
        )
    return out
