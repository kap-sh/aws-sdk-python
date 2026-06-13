"""Generated from Smithy shape ``com.amazonaws.backup#ListIndexedRecoveryPointsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.indexed_recovery_point_list
    import aws_sdk_backup.types.string


class ListIndexedRecoveryPointsOutput(TypedDict):
    indexed_recovery_points: NotRequired[
        "aws_sdk_backup.types.indexed_recovery_point_list.IndexedRecoveryPointList"
    ]
    """<p>This is a list of recovery points that have an associated index, belonging to the specified account.</p>"""
    next_token: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>The next item following a partial list of returned recovery points.</p> <p>For example, if a request is made to return <code>MaxResults</code> number of indexed recovery points, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIndexedRecoveryPointsOutput) -> dict:
    out: dict = {}
    if "indexed_recovery_points" in value:
        import aws_sdk_backup.types.indexed_recovery_point_list

        out["IndexedRecoveryPoints"] = (
            aws_sdk_backup.types.indexed_recovery_point_list.serialize_json(
                value["indexed_recovery_points"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIndexedRecoveryPointsOutput:
    out: ListIndexedRecoveryPointsOutput = {}  # type: ignore[typeddict-item]
    if "IndexedRecoveryPoints" in data:
        import aws_sdk_backup.types.indexed_recovery_point_list

        out["indexed_recovery_points"] = (
            aws_sdk_backup.types.indexed_recovery_point_list.deserialize_json(
                data["IndexedRecoveryPoints"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
