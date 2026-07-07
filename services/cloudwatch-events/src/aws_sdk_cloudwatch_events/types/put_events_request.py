"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#PutEventsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudwatch_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.put_events_request_entry_list


class PutEventsRequest(TypedDict, closed=True):
    entries: "aws_sdk_cloudwatch_events.types.put_events_request_entry_list.PutEventsRequestEntryList"
    """<p>The entry that defines an event in your system. You can specify several parameters for the entry such as the source and type of the event, resources associated with the event, and so on.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutEventsRequest) -> dict:
    out: dict = {}
    import aws_sdk_cloudwatch_events.types.put_events_request_entry_list

    out["Entries"] = (
        aws_sdk_cloudwatch_events.types.put_events_request_entry_list.serialize_aws_json_1_1(
            value["entries"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutEventsRequest:
    out: PutEventsRequest = {}  # type: ignore[typeddict-item]
    if "Entries" in data:
        import aws_sdk_cloudwatch_events.types.put_events_request_entry_list

        out["entries"] = (
            aws_sdk_cloudwatch_events.types.put_events_request_entry_list.deserialize_aws_json_1_1(
                data["Entries"]
            )
        )
    else:
        raise DeserializationError("PutEventsRequest.entries required")
    return out
