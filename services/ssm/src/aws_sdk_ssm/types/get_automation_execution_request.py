"""Generated from Smithy shape ``com.amazonaws.ssm#GetAutomationExecutionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.automation_execution_id


class GetAutomationExecutionRequest(TypedDict):
    automation_execution_id: (
        "aws_sdk_ssm.types.automation_execution_id.AutomationExecutionId"
    )
    """<p>The unique identifier for an existing automation execution to examine. The execution ID is returned by StartAutomationExecution when the execution of an Automation runbook is initiated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAutomationExecutionRequest) -> dict:
    out: dict = {}
    out["AutomationExecutionId"] = value["automation_execution_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAutomationExecutionRequest:
    out: GetAutomationExecutionRequest = {}  # type: ignore[typeddict-item]
    if "AutomationExecutionId" in data:
        out["automation_execution_id"] = data["AutomationExecutionId"]
    else:
        raise DeserializationError(
            "GetAutomationExecutionRequest.automation_execution_id required"
        )
    return out
