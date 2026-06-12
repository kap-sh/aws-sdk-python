"""Generated from Smithy shape ``com.amazonaws.ssm#StopAutomationExecutionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.automation_execution_id
    import aws_sdk_ssm.types.stop_type


class StopAutomationExecutionRequest(TypedDict):
    automation_execution_id: (
        "aws_sdk_ssm.types.automation_execution_id.AutomationExecutionId"
    )
    """<p>The execution ID of the Automation to stop.</p>"""
    type: NotRequired["aws_sdk_ssm.types.stop_type.StopType"]
    """<p>The stop request type. Valid types include the following: Cancel and Complete. The default type is Cancel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopAutomationExecutionRequest) -> dict:
    out: dict = {}
    out["AutomationExecutionId"] = value["automation_execution_id"]
    if "type" in value:
        import aws_sdk_ssm.types.stop_type

        out["Type"] = aws_sdk_ssm.types.stop_type.serialize_aws_json_1_1(value["type"])
    return out


def deserialize_aws_json_1_1(data: dict) -> StopAutomationExecutionRequest:
    out: StopAutomationExecutionRequest = {}  # type: ignore[typeddict-item]
    if "AutomationExecutionId" in data:
        out["automation_execution_id"] = data["AutomationExecutionId"]
    else:
        raise DeserializationError(
            "StopAutomationExecutionRequest.automation_execution_id required"
        )
    if "Type" in data:
        import aws_sdk_ssm.types.stop_type

        out["type"] = aws_sdk_ssm.types.stop_type.deserialize_aws_json_1_1(data["Type"])
    return out
