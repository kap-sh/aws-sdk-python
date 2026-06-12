"""Generated from Smithy shape ``com.amazonaws.swf#FailWorkflowExecutionDecisionAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_swf.types.data
    import aws_sdk_swf.types.failure_reason


class FailWorkflowExecutionDecisionAttributes(TypedDict):
    reason: NotRequired["aws_sdk_swf.types.failure_reason.FailureReason"]
    """<p>A descriptive reason for the failure that may help in diagnostics.</p>"""
    details: NotRequired["aws_sdk_swf.types.data.Data"]
    """<p> Details of the failure.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FailWorkflowExecutionDecisionAttributes) -> dict:
    out: dict = {}
    if "reason" in value:
        out["reason"] = value["reason"]
    if "details" in value:
        out["details"] = value["details"]
    return out


def deserialize_aws_json_1_0(data: dict) -> FailWorkflowExecutionDecisionAttributes:
    out: FailWorkflowExecutionDecisionAttributes = {}  # type: ignore[typeddict-item]
    if "reason" in data:
        out["reason"] = data["reason"]
    if "details" in data:
        out["details"] = data["details"]
    return out
