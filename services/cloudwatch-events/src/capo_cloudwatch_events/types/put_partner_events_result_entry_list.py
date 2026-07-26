"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#PutPartnerEventsResultEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.put_partner_events_result_entry

PutPartnerEventsResultEntryList: TypeAlias = list[
    "capo_cloudwatch_events.types.put_partner_events_result_entry.PutPartnerEventsResultEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutPartnerEventsResultEntryList) -> list:
    import capo_cloudwatch_events.types.put_partner_events_result_entry

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch_events.types.put_partner_events_result_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PutPartnerEventsResultEntryList:
    import capo_cloudwatch_events.types.put_partner_events_result_entry

    out: PutPartnerEventsResultEntryList = []
    for item in data:
        out.append(
            capo_cloudwatch_events.types.put_partner_events_result_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
