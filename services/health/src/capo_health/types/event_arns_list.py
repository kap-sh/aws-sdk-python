"""Generated from Smithy shape ``com.amazonaws.health#EventArnsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.event_arn

EventArnsList: TypeAlias = list["capo_health.types.event_arn.eventArn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventArnsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> EventArnsList:
    return list(data)
