"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#PutPartnerEventsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudwatch_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.put_partner_events_request_entry_list


class PutPartnerEventsRequest(TypedDict):
    entries: "aws_sdk_cloudwatch_events.types.put_partner_events_request_entry_list.PutPartnerEventsRequestEntryList"
    """<p>The list of events to write to the event bus.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutPartnerEventsRequest) -> dict:
    out: dict = {}
    import aws_sdk_cloudwatch_events.types.put_partner_events_request_entry_list

    out["Entries"] = (
        aws_sdk_cloudwatch_events.types.put_partner_events_request_entry_list.serialize_aws_json_1_1(
            value["entries"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutPartnerEventsRequest:
    out: PutPartnerEventsRequest = {}  # type: ignore[typeddict-item]
    if "Entries" in data:
        import aws_sdk_cloudwatch_events.types.put_partner_events_request_entry_list

        out["entries"] = (
            aws_sdk_cloudwatch_events.types.put_partner_events_request_entry_list.deserialize_aws_json_1_1(
                data["Entries"]
            )
        )
    else:
        raise DeserializationError("PutPartnerEventsRequest.entries required")
    return out
