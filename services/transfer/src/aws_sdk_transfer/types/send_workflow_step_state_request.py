"""Generated from Smithy shape ``com.amazonaws.transfer#SendWorkflowStepStateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.callback_token
    import aws_sdk_transfer.types.custom_step_status
    import aws_sdk_transfer.types.execution_id
    import aws_sdk_transfer.types.workflow_id


class SendWorkflowStepStateRequest(TypedDict, closed=True):
    workflow_id: "aws_sdk_transfer.types.workflow_id.WorkflowId"
    """<p>A unique identifier for the workflow.</p>"""
    execution_id: "aws_sdk_transfer.types.execution_id.ExecutionId"
    """<p>A unique identifier for the execution of a workflow.</p>"""
    token: "aws_sdk_transfer.types.callback_token.CallbackToken"
    """<p>Used to distinguish between multiple callbacks for multiple Lambda steps within the same execution.</p>"""
    status: "aws_sdk_transfer.types.custom_step_status.CustomStepStatus"
    """<p>Indicates whether the specified step succeeded or failed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SendWorkflowStepStateRequest) -> dict:
    out: dict = {}
    out["WorkflowId"] = value["workflow_id"]
    out["ExecutionId"] = value["execution_id"]
    out["Token"] = value["token"]
    import aws_sdk_transfer.types.custom_step_status

    out["Status"] = aws_sdk_transfer.types.custom_step_status.serialize_aws_json_1_1(
        value["status"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SendWorkflowStepStateRequest:
    out: SendWorkflowStepStateRequest = {}  # type: ignore[typeddict-item]
    if "WorkflowId" in data:
        out["workflow_id"] = data["WorkflowId"]
    else:
        raise DeserializationError("SendWorkflowStepStateRequest.workflow_id required")
    if "ExecutionId" in data:
        out["execution_id"] = data["ExecutionId"]
    else:
        raise DeserializationError("SendWorkflowStepStateRequest.execution_id required")
    if "Token" in data:
        out["token"] = data["Token"]
    else:
        raise DeserializationError("SendWorkflowStepStateRequest.token required")
    if "Status" in data:
        import aws_sdk_transfer.types.custom_step_status

        out["status"] = (
            aws_sdk_transfer.types.custom_step_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("SendWorkflowStepStateRequest.status required")
    return out
