"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#EventBusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.event_bus

EventBusList: TypeAlias = list["aws_sdk_cloudwatch_events.types.event_bus.EventBus"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventBusList) -> list:
    import aws_sdk_cloudwatch_events.types.event_bus

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch_events.types.event_bus.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EventBusList:
    import aws_sdk_cloudwatch_events.types.event_bus

    out: EventBusList = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_events.types.event_bus.deserialize_aws_json_1_1(item)
        )
    return out
