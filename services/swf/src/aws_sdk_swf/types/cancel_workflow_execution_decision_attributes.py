"""Generated from Smithy shape ``com.amazonaws.swf#CancelWorkflowExecutionDecisionAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_swf.types.data


class CancelWorkflowExecutionDecisionAttributes(TypedDict):
    details: NotRequired["aws_sdk_swf.types.data.Data"]
    """<p> Details of the cancellation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelWorkflowExecutionDecisionAttributes) -> dict:
    out: dict = {}
    if "details" in value:
        out["details"] = value["details"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelWorkflowExecutionDecisionAttributes:
    out: CancelWorkflowExecutionDecisionAttributes = {}  # type: ignore[typeddict-item]
    if "details" in data:
        out["details"] = data["details"]
    return out
