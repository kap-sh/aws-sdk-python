"""Generated from Smithy shape ``com.amazonaws.eventbridge#PartnerEventSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eventbridge.types.partner_event_source

PartnerEventSourceList: TypeAlias = list[
    "capo_eventbridge.types.partner_event_source.PartnerEventSource"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartnerEventSourceList) -> list:
    import capo_eventbridge.types.partner_event_source

    out: list = []
    for item in value:
        out.append(
            capo_eventbridge.types.partner_event_source.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PartnerEventSourceList:
    import capo_eventbridge.types.partner_event_source

    out: PartnerEventSourceList = []
    for item in data:
        out.append(
            capo_eventbridge.types.partner_event_source.deserialize_aws_json_1_1(item)
        )
    return out
