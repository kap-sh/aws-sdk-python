"""Generated from Smithy shape ``com.amazonaws.codecommit#ApprovalStateChangedEventMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.approval_state
    import capo_codecommit.types.revision_id


class ApprovalStateChangedEventMetadata(TypedDict, closed=True):
    revision_id: NotRequired["capo_codecommit.types.revision_id.RevisionId"]
    """<p>The revision ID of the pull request when the approval state changed.</p>"""
    approval_status: NotRequired["capo_codecommit.types.approval_state.ApprovalState"]
    """<p>The approval status for the pull request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApprovalStateChangedEventMetadata) -> dict:
    out: dict = {}
    if "revision_id" in value:
        out["revisionId"] = value["revision_id"]
    if "approval_status" in value:
        import capo_codecommit.types.approval_state

        out["approvalStatus"] = (
            capo_codecommit.types.approval_state.serialize_aws_json_1_1(
                value["approval_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApprovalStateChangedEventMetadata:
    out: ApprovalStateChangedEventMetadata = {}  # type: ignore[typeddict-item]
    if "revisionId" in data:
        out["revision_id"] = data["revisionId"]
    if "approvalStatus" in data:
        import capo_codecommit.types.approval_state

        out["approval_status"] = (
            capo_codecommit.types.approval_state.deserialize_aws_json_1_1(
                data["approvalStatus"]
            )
        )
    return out
