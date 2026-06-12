"""Generated from Smithy shape ``com.amazonaws.codepipeline#PutApprovalResultOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.timestamp


class PutApprovalResultOutput(TypedDict):
    approved_at: NotRequired["aws_sdk_codepipeline.types.timestamp.Timestamp"]
    """<p>The timestamp showing when the approval or rejection was submitted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutApprovalResultOutput) -> dict:
    out: dict = {}
    if "approved_at" in value:
        import aws_sdk_codepipeline.types.timestamp

        out["approvedAt"] = aws_sdk_codepipeline.types.timestamp.serialize_aws_json_1_1(
            value["approved_at"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutApprovalResultOutput:
    out: PutApprovalResultOutput = {}  # type: ignore[typeddict-item]
    if "approvedAt" in data:
        import aws_sdk_codepipeline.types.timestamp

        out["approved_at"] = (
            aws_sdk_codepipeline.types.timestamp.deserialize_aws_json_1_1(
                data["approvedAt"]
            )
        )
    return out
