"""Generated from Smithy shape ``com.amazonaws.mpa#StartActiveApprovalTeamDeletionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mpa.types.iso_timestamp


class StartActiveApprovalTeamDeletionResponse(TypedDict):
    deletion_completion_time: NotRequired[
        "aws_sdk_mpa.types.iso_timestamp.IsoTimestamp"
    ]
    """<p>Timestamp when the deletion process is scheduled to complete.</p>"""
    deletion_start_time: NotRequired["aws_sdk_mpa.types.iso_timestamp.IsoTimestamp"]
    """<p>Timestamp when the deletion process was initiated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartActiveApprovalTeamDeletionResponse) -> dict:
    out: dict = {}
    if "deletion_completion_time" in value:
        import aws_sdk_mpa.types.iso_timestamp

        out["DeletionCompletionTime"] = aws_sdk_mpa.types.iso_timestamp.serialize_json(
            value["deletion_completion_time"]
        )
    if "deletion_start_time" in value:
        import aws_sdk_mpa.types.iso_timestamp

        out["DeletionStartTime"] = aws_sdk_mpa.types.iso_timestamp.serialize_json(
            value["deletion_start_time"]
        )
    return out


def deserialize_json(data: dict) -> StartActiveApprovalTeamDeletionResponse:
    out: StartActiveApprovalTeamDeletionResponse = {}  # type: ignore[typeddict-item]
    if "DeletionCompletionTime" in data:
        import aws_sdk_mpa.types.iso_timestamp

        out["deletion_completion_time"] = (
            aws_sdk_mpa.types.iso_timestamp.deserialize_json(
                data["DeletionCompletionTime"]
            )
        )
    if "DeletionStartTime" in data:
        import aws_sdk_mpa.types.iso_timestamp

        out["deletion_start_time"] = aws_sdk_mpa.types.iso_timestamp.deserialize_json(
            data["DeletionStartTime"]
        )
    return out
