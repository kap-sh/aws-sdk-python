"""Generated from Smithy shape ``com.amazonaws.mpa#StartActiveApprovalTeamDeletionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mpa.types.iso_timestamp


class StartActiveApprovalTeamDeletionResponse(TypedDict, closed=True):
    deletion_completion_time: NotRequired["capo_mpa.types.iso_timestamp.IsoTimestamp"]
    """<p>Timestamp when the deletion process is scheduled to complete.</p>"""
    deletion_start_time: NotRequired["capo_mpa.types.iso_timestamp.IsoTimestamp"]
    """<p>Timestamp when the deletion process was initiated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartActiveApprovalTeamDeletionResponse) -> dict:
    out: dict = {}
    if "deletion_completion_time" in value:
        import capo_mpa.types.iso_timestamp

        out["DeletionCompletionTime"] = capo_mpa.types.iso_timestamp.serialize_json(
            value["deletion_completion_time"]
        )
    if "deletion_start_time" in value:
        import capo_mpa.types.iso_timestamp

        out["DeletionStartTime"] = capo_mpa.types.iso_timestamp.serialize_json(
            value["deletion_start_time"]
        )
    return out


def deserialize_json(data: dict) -> StartActiveApprovalTeamDeletionResponse:
    out: StartActiveApprovalTeamDeletionResponse = {}  # type: ignore[typeddict-item]
    if "DeletionCompletionTime" in data:
        import capo_mpa.types.iso_timestamp

        out["deletion_completion_time"] = capo_mpa.types.iso_timestamp.deserialize_json(
            data["DeletionCompletionTime"]
        )
    if "DeletionStartTime" in data:
        import capo_mpa.types.iso_timestamp

        out["deletion_start_time"] = capo_mpa.types.iso_timestamp.deserialize_json(
            data["DeletionStartTime"]
        )
    return out
