"""Generated from Smithy shape ``com.amazonaws.eventbridge#PutEventsRequestEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.put_events_request_entry

PutEventsRequestEntryList: TypeAlias = list[
    "aws_sdk_eventbridge.types.put_events_request_entry.PutEventsRequestEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutEventsRequestEntryList) -> list:
    import aws_sdk_eventbridge.types.put_events_request_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_eventbridge.types.put_events_request_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PutEventsRequestEntryList:
    import aws_sdk_eventbridge.types.put_events_request_entry

    out: PutEventsRequestEntryList = []
    for item in data:
        out.append(
            aws_sdk_eventbridge.types.put_events_request_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
