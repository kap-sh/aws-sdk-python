"""Generated from Smithy shape ``com.amazonaws.swf#DecisionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_swf.errors import DeserializationError

DecisionType: TypeAlias = Literal[
    "ScheduleActivityTask",
    "RequestCancelActivityTask",
    "CompleteWorkflowExecution",
    "FailWorkflowExecution",
    "CancelWorkflowExecution",
    "ContinueAsNewWorkflowExecution",
    "RecordMarker",
    "StartTimer",
    "CancelTimer",
    "SignalExternalWorkflowExecution",
    "RequestCancelExternalWorkflowExecution",
    "StartChildWorkflowExecution",
    "ScheduleLambdaFunction",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ScheduleActivityTask",
        "RequestCancelActivityTask",
        "CompleteWorkflowExecution",
        "FailWorkflowExecution",
        "CancelWorkflowExecution",
        "ContinueAsNewWorkflowExecution",
        "RecordMarker",
        "StartTimer",
        "CancelTimer",
        "SignalExternalWorkflowExecution",
        "RequestCancelExternalWorkflowExecution",
        "StartChildWorkflowExecution",
        "ScheduleLambdaFunction",
    )
)


def serialize_aws_json_1_0(value: DecisionType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DecisionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DecisionType value: {data!r}")
    return cast(DecisionType, data)
