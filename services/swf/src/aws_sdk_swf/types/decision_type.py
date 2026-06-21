"""Generated from Smithy shape ``com.amazonaws.swf#DecisionType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_0(value: DecisionType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DecisionType:
    return cast(DecisionType, data)
