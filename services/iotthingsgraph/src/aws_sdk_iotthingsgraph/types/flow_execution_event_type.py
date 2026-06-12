"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#FlowExecutionEventType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotthingsgraph.errors import DeserializationError

FlowExecutionEventType: TypeAlias = Literal[
    "EXECUTION_STARTED",
    "EXECUTION_FAILED",
    "EXECUTION_ABORTED",
    "EXECUTION_SUCCEEDED",
    "STEP_STARTED",
    "STEP_FAILED",
    "STEP_SUCCEEDED",
    "ACTIVITY_SCHEDULED",
    "ACTIVITY_STARTED",
    "ACTIVITY_FAILED",
    "ACTIVITY_SUCCEEDED",
    "START_FLOW_EXECUTION_TASK",
    "SCHEDULE_NEXT_READY_STEPS_TASK",
    "THING_ACTION_TASK",
    "THING_ACTION_TASK_FAILED",
    "THING_ACTION_TASK_SUCCEEDED",
    "ACKNOWLEDGE_TASK_MESSAGE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EXECUTION_STARTED",
        "EXECUTION_FAILED",
        "EXECUTION_ABORTED",
        "EXECUTION_SUCCEEDED",
        "STEP_STARTED",
        "STEP_FAILED",
        "STEP_SUCCEEDED",
        "ACTIVITY_SCHEDULED",
        "ACTIVITY_STARTED",
        "ACTIVITY_FAILED",
        "ACTIVITY_SUCCEEDED",
        "START_FLOW_EXECUTION_TASK",
        "SCHEDULE_NEXT_READY_STEPS_TASK",
        "THING_ACTION_TASK",
        "THING_ACTION_TASK_FAILED",
        "THING_ACTION_TASK_SUCCEEDED",
        "ACKNOWLEDGE_TASK_MESSAGE",
    )
)


def serialize_aws_json_1_1(value: FlowExecutionEventType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FlowExecutionEventType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FlowExecutionEventType value: {data!r}")
    return cast(FlowExecutionEventType, data)
