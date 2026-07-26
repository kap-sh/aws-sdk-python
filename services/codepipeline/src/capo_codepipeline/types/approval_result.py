"""Generated from Smithy shape ``com.amazonaws.codepipeline#ApprovalResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codepipeline.types.approval_status
    import capo_codepipeline.types.approval_summary


class ApprovalResult(TypedDict, closed=True):
    summary: "capo_codepipeline.types.approval_summary.ApprovalSummary"
    """<p>The summary of the current status of the approval request.</p>"""
    status: "capo_codepipeline.types.approval_status.ApprovalStatus"
    """<p>The response submitted by a reviewer assigned to an approval action request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApprovalResult) -> dict:
    out: dict = {}
    out["summary"] = value["summary"]
    import capo_codepipeline.types.approval_status

    out["status"] = capo_codepipeline.types.approval_status.serialize_aws_json_1_1(
        value["status"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApprovalResult:
    out: ApprovalResult = {}  # type: ignore[typeddict-item]
    if "summary" in data:
        out["summary"] = data["summary"]
    else:
        raise DeserializationError("ApprovalResult.summary required")
    if "status" in data:
        import capo_codepipeline.types.approval_status

        out["status"] = (
            capo_codepipeline.types.approval_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    else:
        raise DeserializationError("ApprovalResult.status required")
    return out
