"""Generated from Smithy shape ``com.amazonaws.ssm#GetAutomationExecutionResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.automation_execution


class GetAutomationExecutionResult(TypedDict):
    automation_execution: NotRequired[
        "aws_sdk_ssm.types.automation_execution.AutomationExecution"
    ]
    """<p>Detailed information about the current state of an automation execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAutomationExecutionResult) -> dict:
    out: dict = {}
    if "automation_execution" in value:
        import aws_sdk_ssm.types.automation_execution

        out["AutomationExecution"] = (
            aws_sdk_ssm.types.automation_execution.serialize_aws_json_1_1(
                value["automation_execution"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAutomationExecutionResult:
    out: GetAutomationExecutionResult = {}  # type: ignore[typeddict-item]
    if "AutomationExecution" in data:
        import aws_sdk_ssm.types.automation_execution

        out["automation_execution"] = (
            aws_sdk_ssm.types.automation_execution.deserialize_aws_json_1_1(
                data["AutomationExecution"]
            )
        )
    return out
