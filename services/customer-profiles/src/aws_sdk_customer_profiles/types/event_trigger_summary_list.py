"""Generated from Smithy shape ``com.amazonaws.customerprofiles#EventTriggerSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.event_trigger_summary_item

EventTriggerSummaryList: TypeAlias = list[
    "aws_sdk_customer_profiles.types.event_trigger_summary_item.EventTriggerSummaryItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: EventTriggerSummaryList) -> list:
    import aws_sdk_customer_profiles.types.event_trigger_summary_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_customer_profiles.types.event_trigger_summary_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> EventTriggerSummaryList:
    import aws_sdk_customer_profiles.types.event_trigger_summary_item

    out: EventTriggerSummaryList = []
    for item in data:
        out.append(
            aws_sdk_customer_profiles.types.event_trigger_summary_item.deserialize_json(
                item
            )
        )
    return out
