"""Generated from Smithy shape ``com.amazonaws.codepipeline#ApprovalResult``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.approval_status
    import aws_sdk_codepipeline.types.approval_summary


class ApprovalResult(TypedDict):
    summary: "aws_sdk_codepipeline.types.approval_summary.ApprovalSummary"
    """<p>The summary of the current status of the approval request.</p>"""
    status: "aws_sdk_codepipeline.types.approval_status.ApprovalStatus"
    """<p>The response submitted by a reviewer assigned to an approval action request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApprovalResult) -> dict:
    out: dict = {}
    out["summary"] = value["summary"]
    import aws_sdk_codepipeline.types.approval_status

    out["status"] = aws_sdk_codepipeline.types.approval_status.serialize_aws_json_1_1(
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
        import aws_sdk_codepipeline.types.approval_status

        out["status"] = (
            aws_sdk_codepipeline.types.approval_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    else:
        raise DeserializationError("ApprovalResult.status required")
    return out
