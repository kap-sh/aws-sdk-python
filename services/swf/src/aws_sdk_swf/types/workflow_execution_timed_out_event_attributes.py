"""Generated from Smithy shape ``com.amazonaws.swf#WorkflowExecutionTimedOutEventAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.child_policy
    import aws_sdk_swf.types.workflow_execution_timeout_type


class WorkflowExecutionTimedOutEventAttributes(TypedDict, closed=True):
    timeout_type: (
        "aws_sdk_swf.types.workflow_execution_timeout_type.WorkflowExecutionTimeoutType"
    )
    """<p>The type of timeout that caused this event.</p>"""
    child_policy: "aws_sdk_swf.types.child_policy.ChildPolicy"
    """<p>The policy used for the child workflow executions of this workflow execution.</p> <p>The supported child policies are:</p> <ul> <li> <p> <code>TERMINATE</code> – The child executions are terminated.</p> </li> <li> <p> <code>REQUEST_CANCEL</code> – A request to cancel is attempted for each child execution by recording a <code>WorkflowExecutionCancelRequested</code> event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.</p> </li> <li> <p> <code>ABANDON</code> – No action is taken. The child executions continue to run.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowExecutionTimedOutEventAttributes) -> dict:
    out: dict = {}
    import aws_sdk_swf.types.workflow_execution_timeout_type

    out["timeoutType"] = (
        aws_sdk_swf.types.workflow_execution_timeout_type.serialize_aws_json_1_0(
            value["timeout_type"]
        )
    )
    import aws_sdk_swf.types.child_policy

    out["childPolicy"] = aws_sdk_swf.types.child_policy.serialize_aws_json_1_0(
        value["child_policy"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkflowExecutionTimedOutEventAttributes:
    out: WorkflowExecutionTimedOutEventAttributes = {}  # type: ignore[typeddict-item]
    if "timeoutType" in data:
        import aws_sdk_swf.types.workflow_execution_timeout_type

        out["timeout_type"] = (
            aws_sdk_swf.types.workflow_execution_timeout_type.deserialize_aws_json_1_0(
                data["timeoutType"]
            )
        )
    else:
        raise DeserializationError(
            "WorkflowExecutionTimedOutEventAttributes.timeout_type required"
        )
    if "childPolicy" in data:
        import aws_sdk_swf.types.child_policy

        out["child_policy"] = aws_sdk_swf.types.child_policy.deserialize_aws_json_1_0(
            data["childPolicy"]
        )
    else:
        raise DeserializationError(
            "WorkflowExecutionTimedOutEventAttributes.child_policy required"
        )
    return out
