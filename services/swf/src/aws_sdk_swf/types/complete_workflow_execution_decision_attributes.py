"""Generated from Smithy shape ``com.amazonaws.swf#CompleteWorkflowExecutionDecisionAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_swf.types.data


class CompleteWorkflowExecutionDecisionAttributes(TypedDict):
    result: NotRequired["aws_sdk_swf.types.data.Data"]
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
