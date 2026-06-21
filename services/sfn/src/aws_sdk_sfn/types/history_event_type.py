"""Generated from Smithy shape ``com.amazonaws.sfn#HistoryEventType``."""

from typing import Literal, TypeAlias, cast

HistoryEventType: TypeAlias = Literal[
    "ActivityFailed",
    "ActivityScheduled",
    "ActivityScheduleFailed",
    "ActivityStarted",
    "ActivitySucceeded",
    "ActivityTimedOut",
    "ChoiceStateEntered",
    "ChoiceStateExited",
    "ExecutionAborted",
    "ExecutionFailed",
    "ExecutionStarted",
    "ExecutionSucceeded",
    "ExecutionTimedOut",
    "FailStateEntered",
    "LambdaFunctionFailed",
    "LambdaFunctionScheduled",
    "LambdaFunctionScheduleFailed",
    "LambdaFunctionStarted",
    "LambdaFunctionStartFailed",
    "LambdaFunctionSucceeded",
    "LambdaFunctionTimedOut",
    "MapIterationAborted",
    "MapIterationFailed",
    "MapIterationStarted",
    "MapIterationSucceeded",
    "MapStateAborted",
    "MapStateEntered",
    "MapStateExited",
    "MapStateFailed",
    "MapStateStarted",
    "MapStateSucceeded",
    "ParallelStateAborted",
    "ParallelStateEntered",
    "ParallelStateExited",
    "ParallelStateFailed",
    "ParallelStateStarted",
    "ParallelStateSucceeded",
    "PassStateEntered",
    "PassStateExited",
    "SucceedStateEntered",
    "SucceedStateExited",
    "TaskFailed",
    "TaskScheduled",
    "TaskStarted",
    "TaskStartFailed",
    "TaskStateAborted",
    "TaskStateEntered",
    "TaskStateExited",
    "TaskSubmitFailed",
    "TaskSubmitted",
    "TaskSucceeded",
    "TaskTimedOut",
    "WaitStateAborted",
    "WaitStateEntered",
    "WaitStateExited",
    "MapRunAborted",
    "MapRunFailed",
    "MapRunStarted",
    "MapRunSucceeded",
    "ExecutionRedriven",
    "MapRunRedriven",
    "EvaluationFailed",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HistoryEventType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> HistoryEventType:
    return cast(HistoryEventType, data)
