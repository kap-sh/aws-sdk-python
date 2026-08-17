"""Generated from Smithy shape ``com.amazonaws.ssm#StartAutomationExecutionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.automation_execution_id


class StartAutomationExecutionResult(TypedDict, closed=True):
    automation_execution_id: NotRequired[
        "capo_ssm.types.automation_execution_id.AutomationExecutionId"
    ]
    """<p>The unique ID of a newly scheduled automation execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartAutomationExecutionResult) -> dict:
    out: dict = {}
    if "automation_execution_id" in value:
        out["AutomationExecutionId"] = value["automation_execution_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartAutomationExecutionResult:
    out: StartAutomationExecutionResult = {}  # type: ignore[typeddict-item]
    if data.get("AutomationExecutionId") is not None:
        out["automation_execution_id"] = data["AutomationExecutionId"]
    return out
