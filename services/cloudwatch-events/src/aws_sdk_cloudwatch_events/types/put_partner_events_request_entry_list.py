"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#PutPartnerEventsRequestEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.put_partner_events_request_entry

PutPartnerEventsRequestEntryList: TypeAlias = list[
    "aws_sdk_cloudwatch_events.types.put_partner_events_request_entry.PutPartnerEventsRequestEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutPartnerEventsRequestEntryList) -> list:
    import aws_sdk_cloudwatch_events.types.put_partner_events_request_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch_events.types.put_partner_events_request_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PutPartnerEventsRequestEntryList:
    import aws_sdk_cloudwatch_events.types.put_partner_events_request_entry

    out: PutPartnerEventsRequestEntryList = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_events.types.put_partner_events_request_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
