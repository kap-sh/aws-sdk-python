"""Generated from Smithy shape ``com.amazonaws.backup#ListRecoveryPointsByLegalHoldOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.recovery_points_list
    import aws_sdk_backup.types.string


class ListRecoveryPointsByLegalHoldOutput(TypedDict, closed=True):
    recovery_points: NotRequired[
        "aws_sdk_backup.types.recovery_points_list.RecoveryPointsList"
    ]
    """<p>The recovery points.</p>"""
    next_token: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>The next item following a partial list of returned resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecoveryPointsByLegalHoldOutput) -> dict:
    out: dict = {}
    if "recovery_points" in value:
        import aws_sdk_backup.types.recovery_points_list

        out["RecoveryPoints"] = (
            aws_sdk_backup.types.recovery_points_list.serialize_json(
                value["recovery_points"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRecoveryPointsByLegalHoldOutput:
    out: ListRecoveryPointsByLegalHoldOutput = {}  # type: ignore[typeddict-item]
    if "RecoveryPoints" in data:
        import aws_sdk_backup.types.recovery_points_list

        out["recovery_points"] = (
            aws_sdk_backup.types.recovery_points_list.deserialize_json(
                data["RecoveryPoints"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
