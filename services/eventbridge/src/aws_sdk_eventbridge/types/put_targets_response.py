"""Generated from Smithy shape ``com.amazonaws.eventbridge#PutTargetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.integer
    import aws_sdk_eventbridge.types.put_targets_result_entry_list


class PutTargetsResponse(TypedDict, closed=True):
    failed_entry_count: "aws_sdk_eventbridge.types.integer.Integer"
    """<p>The number of failed entries.</p>"""
    failed_entries: NotRequired[
        "aws_sdk_eventbridge.types.put_targets_result_entry_list.PutTargetsResultEntryList"
    ]
    """<p>The failed target entries.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutTargetsResponse) -> dict:
    out: dict = {}
    out["FailedEntryCount"] = value.get("failed_entry_count", 0)
    if "failed_entries" in value:
        import aws_sdk_eventbridge.types.put_targets_result_entry_list

        out["FailedEntries"] = (
            aws_sdk_eventbridge.types.put_targets_result_entry_list.serialize_aws_json_1_1(
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
        import aws_sdk_eventbridge.types.put_targets_result_entry_list

        out["failed_entries"] = (
            aws_sdk_eventbridge.types.put_targets_result_entry_list.deserialize_aws_json_1_1(
                data["FailedEntries"]
            )
        )
    return out
