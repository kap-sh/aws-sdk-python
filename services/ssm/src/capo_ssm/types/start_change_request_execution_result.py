"""Generated from Smithy shape ``com.amazonaws.ssm#StartChangeRequestExecutionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.automation_execution_id


class StartChangeRequestExecutionResult(TypedDict, closed=True):
    automation_execution_id: NotRequired[
        "capo_ssm.types.automation_execution_id.AutomationExecutionId"
    ]
    """<p>The unique ID of a runbook workflow operation. (A runbook workflow is a type of Automation operation.) </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartChangeRequestExecutionResult) -> dict:
    out: dict = {}
    if "automation_execution_id" in value:
        out["AutomationExecutionId"] = value["automation_execution_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartChangeRequestExecutionResult:
    out: StartChangeRequestExecutionResult = {}  # type: ignore[typeddict-item]
    if data.get("AutomationExecutionId") is not None:
        out["automation_execution_id"] = data["AutomationExecutionId"]
    return out
