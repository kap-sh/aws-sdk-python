"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#PutTargetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.integer
    import capo_cloudwatch_events.types.put_targets_result_entry_list


class PutTargetsResponse(TypedDict, closed=True):
    failed_entry_count: "capo_cloudwatch_events.types.integer.Integer"
    """<p>The number of failed entries.</p>"""
    failed_entries: NotRequired[
        "capo_cloudwatch_events.types.put_targets_result_entry_list.PutTargetsResultEntryList"
    ]
    """<p>The failed target entries.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutTargetsResponse) -> dict:
    out: dict = {}
    out["FailedEntryCount"] = value.get("failed_entry_count", 0)
    if "failed_entries" in value:
        import capo_cloudwatch_events.types.put_targets_result_entry_list

        out["FailedEntries"] = (
            capo_cloudwatch_events.types.put_targets_result_entry_list.serialize_aws_json_1_1(
                value["failed_entries"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutTargetsResponse:
    out: PutTargetsResponse = {}  # type: ignore[typeddict-item]
    if "FailedEntryCount" in data:
        out["failed_entry_count"] = data["FailedEntryCount"]
    else:
        out["failed_entry_count"] = 0
    if "FailedEntries" in data:
        import capo_cloudwatch_events.types.put_targets_result_entry_list

        out["failed_entries"] = (
            capo_cloudwatch_events.types.put_targets_result_entry_list.deserialize_aws_json_1_1(
                data["FailedEntries"]
            )
        )
    return out
