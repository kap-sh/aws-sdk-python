"""Generated from Smithy shape ``com.amazonaws.backup#ListRecoveryPointsByResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.recovery_point_by_resource_list
    import capo_backup.types.string


class ListRecoveryPointsByResourceOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_backup.types.string.string"]
    """<p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""
    recovery_points: NotRequired[
        "capo_backup.types.recovery_point_by_resource_list.RecoveryPointByResourceList"
    ]
    """<p>An array of objects that contain detailed information about recovery points of the specified resource type.</p> <note> <p>Only Amazon EFS and Amazon EC2 recovery points return BackupVaultName.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecoveryPointsByResourceOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "recovery_points" in value:
        import capo_backup.types.recovery_point_by_resource_list

        out["RecoveryPoints"] = (
            capo_backup.types.recovery_point_by_resource_list.serialize_json(
                value["recovery_points"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListRecoveryPointsByResourceOutput:
    out: ListRecoveryPointsByResourceOutput = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RecoveryPoints" in data:
        import capo_backup.types.recovery_point_by_resource_list

        out["recovery_points"] = (
            capo_backup.types.recovery_point_by_resource_list.deserialize_json(
                data["RecoveryPoints"]
            )
        )
    return out
