"""Generated from Smithy shape ``com.amazonaws.eventbridge#EventResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.event_resource

EventResourceList: TypeAlias = list[
    "aws_sdk_eventbridge.types.event_resource.EventResource"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventResourceList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> EventResourceList:
    return list(data)
