"""Generated from Smithy shape ``com.amazonaws.eventbridge#PutPartnerEventsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.integer
    import aws_sdk_eventbridge.types.put_partner_events_result_entry_list


class PutPartnerEventsResponse(TypedDict):
    failed_entry_count: "aws_sdk_eventbridge.types.integer.Integer"
    """<p>The number of events from this operation that could not be written to the partner event bus.</p>"""
    entries: NotRequired[
        "aws_sdk_eventbridge.types.put_partner_events_result_entry_list.PutPartnerEventsResultEntryList"
    ]
    """<p>The results for each event entry the partner submitted in this request. If the event was successfully submitted, the entry has the event ID in it. Otherwise, you can use the error code and error message to identify the problem with the entry.</p> <p>For each record, the index of the response element is the same as the index in the request array.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutPartnerEventsResponse) -> dict:
    out: dict = {}
    out["FailedEntryCount"] = value.get("failed_entry_count", 0)
    if "entries" in value:
        import aws_sdk_eventbridge.types.put_partner_events_result_entry_list

        out["Entries"] = (
            aws_sdk_eventbridge.types.put_partner_events_result_entry_list.serialize_aws_json_1_1(
                value["entries"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutPartnerEventsResponse:
    out: PutPartnerEventsResponse = {}  # type: ignore[typeddict-item]
    if "FailedEntryCount" in data:
        out["failed_entry_count"] = data["FailedEntryCount"]
    else:
        out["failed_entry_count"] = 0
    if "Entries" in data:
        import aws_sdk_eventbridge.types.put_partner_events_result_entry_list

        out["entries"] = (
            aws_sdk_eventbridge.types.put_partner_events_result_entry_list.deserialize_aws_json_1_1(
                data["Entries"]
            )
        )
    return out
