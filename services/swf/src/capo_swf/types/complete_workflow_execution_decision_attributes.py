"""Generated from Smithy shape ``com.amazonaws.swf#CompleteWorkflowExecutionDecisionAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_swf.types.data


class CompleteWorkflowExecutionDecisionAttributes(TypedDict, closed=True):
    result: NotRequired["capo_swf.types.data.Data"]
    """<p>The result of the workflow execution. The form of the result is implementation defined.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CompleteWorkflowExecutionDecisionAttributes) -> dict:
    out: dict = {}
    if "result" in value:
        out["result"] = value["result"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CompleteWorkflowExecutionDecisionAttributes:
    out: CompleteWorkflowExecutionDecisionAttributes = {}  # type: ignore[typeddict-item]
    if "result" in data:
        out["result"] = data["result"]
    return out
