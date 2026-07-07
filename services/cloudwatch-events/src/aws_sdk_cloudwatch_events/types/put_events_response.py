"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#PutEventsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.integer
    import aws_sdk_cloudwatch_events.types.put_events_result_entry_list


class PutEventsResponse(TypedDict, closed=True):
    failed_entry_count: "aws_sdk_cloudwatch_events.types.integer.Integer"
    """<p>The number of failed entries.</p>"""
    entries: NotRequired[
        "aws_sdk_cloudwatch_events.types.put_events_result_entry_list.PutEventsResultEntryList"
    ]
    """<p>The successfully and unsuccessfully ingested events results. If the ingestion was successful, the entry has the event ID in it. Otherwise, you can use the error code and error message to identify the problem with the entry.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutEventsResponse) -> dict:
    out: dict = {}
    out["FailedEntryCount"] = value.get("failed_entry_count", 0)
    if "entries" in value:
        import aws_sdk_cloudwatch_events.types.put_events_result_entry_list

        out["Entries"] = (
            aws_sdk_cloudwatch_events.types.put_events_result_entry_list.serialize_aws_json_1_1(
                value["entries"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutEventsResponse:
    out: PutEventsResponse = {}  # type: ignore[typeddict-item]
    if "FailedEntryCount" in data:
        out["failed_entry_count"] = data["FailedEntryCount"]
    else:
        out["failed_entry_count"] = 0
    if "Entries" in data:
        import aws_sdk_cloudwatch_events.types.put_events_result_entry_list

        out["entries"] = (
            aws_sdk_cloudwatch_events.types.put_events_result_entry_list.deserialize_aws_json_1_1(
                data["Entries"]
            )
        )
    return out
