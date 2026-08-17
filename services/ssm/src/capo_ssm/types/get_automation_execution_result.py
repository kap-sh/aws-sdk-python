"""Generated from Smithy shape ``com.amazonaws.ssm#GetAutomationExecutionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.automation_execution


class GetAutomationExecutionResult(TypedDict, closed=True):
    automation_execution: NotRequired[
        "capo_ssm.types.automation_execution.AutomationExecution"
    ]
    """<p>Detailed information about the current state of an automation execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAutomationExecutionResult) -> dict:
    out: dict = {}
    if "automation_execution" in value:
        import capo_ssm.types.automation_execution

        out["AutomationExecution"] = (
            capo_ssm.types.automation_execution.serialize_aws_json_1_1(
                value["automation_execution"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAutomationExecutionResult:
    out: GetAutomationExecutionResult = {}  # type: ignore[typeddict-item]
    if data.get("AutomationExecution") is not None:
        import capo_ssm.types.automation_execution

        out["automation_execution"] = (
            capo_ssm.types.automation_execution.deserialize_aws_json_1_1(
                data["AutomationExecution"]
            )
        )
    return out
