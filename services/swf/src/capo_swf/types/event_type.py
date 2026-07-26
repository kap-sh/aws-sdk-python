"""Generated from Smithy shape ``com.amazonaws.swf#EventType``."""

from typing import Literal, TypeAlias, cast

EventType: TypeAlias = Literal[
    "WorkflowExecutionStarted",
    "WorkflowExecutionCancelRequested",
    "WorkflowExecutionCompleted",
    "CompleteWorkflowExecutionFailed",
    "WorkflowExecutionFailed",
    "FailWorkflowExecutionFailed",
    "WorkflowExecutionTimedOut",
    "WorkflowExecutionCanceled",
    "CancelWorkflowExecutionFailed",
    "WorkflowExecutionContinuedAsNew",
    "ContinueAsNewWorkflowExecutionFailed",
    "WorkflowExecutionTerminated",
    "DecisionTaskScheduled",
    "DecisionTaskStarted",
    "DecisionTaskCompleted",
    "DecisionTaskTimedOut",
    "ActivityTaskScheduled",
    "ScheduleActivityTaskFailed",
    "ActivityTaskStarted",
    "ActivityTaskCompleted",
    "ActivityTaskFailed",
    "ActivityTaskTimedOut",
    "ActivityTaskCanceled",
    "ActivityTaskCancelRequested",
    "RequestCancelActivityTaskFailed",
    "WorkflowExecutionSignaled",
    "MarkerRecorded",
    "RecordMarkerFailed",
    "TimerStarted",
    "StartTimerFailed",
    "TimerFired",
    "TimerCanceled",
    "CancelTimerFailed",
    "StartChildWorkflowExecutionInitiated",
    "StartChildWorkflowExecutionFailed",
    "ChildWorkflowExecutionStarted",
    "ChildWorkflowExecutionCompleted",
    "ChildWorkflowExecutionFailed",
    "ChildWorkflowExecutionTimedOut",
    "ChildWorkflowExecutionCanceled",
    "ChildWorkflowExecutionTerminated",
    "SignalExternalWorkflowExecutionInitiated",
    "SignalExternalWorkflowExecutionFailed",
    "ExternalWorkflowExecutionSignaled",
    "RequestCancelExternalWorkflowExecutionInitiated",
    "RequestCancelExternalWorkflowExecutionFailed",
    "ExternalWorkflowExecutionCancelRequested",
    "LambdaFunctionScheduled",
    "LambdaFunctionStarted",
    "LambdaFunctionCompleted",
    "LambdaFunctionFailed",
    "LambdaFunctionTimedOut",
    "ScheduleLambdaFunctionFailed",
    "StartLambdaFunctionFailed",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EventType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EventType:
    return cast(EventType, data)
