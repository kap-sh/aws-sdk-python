"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ScheduledQueryDestinationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.scheduled_query_destination

ScheduledQueryDestinationList: TypeAlias = list[
    "capo_cloudwatch_logs.types.scheduled_query_destination.ScheduledQueryDestination"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScheduledQueryDestinationList) -> list:
    import capo_cloudwatch_logs.types.scheduled_query_destination

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch_logs.types.scheduled_query_destination.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ScheduledQueryDestinationList:
    import capo_cloudwatch_logs.types.scheduled_query_destination

    out: ScheduledQueryDestinationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch_logs.types.scheduled_query_destination.deserialize_aws_json_1_1(
                item
            )
        )
    return out
