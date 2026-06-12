"""Generated from Smithy shape ``com.amazonaws.customerprofiles#EventTriggerConditions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.event_trigger_condition

EventTriggerConditions: TypeAlias = list[
    "aws_sdk_customer_profiles.types.event_trigger_condition.EventTriggerCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: EventTriggerConditions) -> list:
    import aws_sdk_customer_profiles.types.event_trigger_condition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_customer_profiles.types.event_trigger_condition.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EventTriggerConditions:
    import aws_sdk_customer_profiles.types.event_trigger_condition

    out: EventTriggerConditions = []
    for item in data:
        out.append(
            aws_sdk_customer_profiles.types.event_trigger_condition.deserialize_json(
                item
            )
        )
    return out
