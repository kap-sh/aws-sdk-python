"""Generated from Smithy shape ``com.amazonaws.eventbridge#PutEventsResultEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eventbridge.types.put_events_result_entry

PutEventsResultEntryList: TypeAlias = list[
    "capo_eventbridge.types.put_events_result_entry.PutEventsResultEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutEventsResultEntryList) -> list:
    import capo_eventbridge.types.put_events_result_entry

    out: list = []
    for item in value:
        out.append(
            capo_eventbridge.types.put_events_result_entry.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PutEventsResultEntryList:
    import capo_eventbridge.types.put_events_result_entry

    out: PutEventsResultEntryList = []
    for item in data:
        out.append(
            capo_eventbridge.types.put_events_result_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
