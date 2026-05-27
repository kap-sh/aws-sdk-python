"""Generated from Smithy shape ``com.amazonaws.eks#CapabilityIssue``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.capability_issue_code
    import aws_sdk_eks.types.string


class CapabilityIssue(TypedDict):
    code: NotRequired["aws_sdk_eks.types.capability_issue_code.CapabilityIssueCode"]
    """<p>A code identifying the type of issue. This can be used to programmatically handle specific issue types.</p>"""
    message: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>A human-readable message describing the issue and potential remediation steps.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityIssue) -> dict:
    out: dict = {}
    if "code" in value:
        import aws_sdk_eks.types.capability_issue_code

        out["code"] = aws_sdk_eks.types.capability_issue_code.serialize_json(
            value["code"]
        )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> CapabilityIssue:
    out: CapabilityIssue = {}  # type: ignore[typeddict-item]
    if "code" in data:
        import aws_sdk_eks.types.capability_issue_code

        out["code"] = aws_sdk_eks.types.capability_issue_code.deserialize_json(
            data["code"]
        )
    if "message" in data:
        out["message"] = data["message"]
    return out
