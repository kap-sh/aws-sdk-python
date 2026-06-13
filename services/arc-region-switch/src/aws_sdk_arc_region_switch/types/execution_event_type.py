"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ExecutionEventType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_region_switch.errors import DeserializationError

ExecutionEventType: TypeAlias = Literal[
    "unknown",
    "executionPending",
    "executionStarted",
    "executionSucceeded",
    "executionFailed",
    "executionPausing",
    "executionPaused",
    "executionCanceling",
    "executionCanceled",
    "executionPendingApproval",
    "executionBehaviorChangedToUngraceful",
    "executionBehaviorChangedToGraceful",
    "executionPendingChildPlanManualApproval",
    "executionSuccessMonitoringApplicationHealth",
    "stepStarted",
    "stepUpdate",
    "stepSucceeded",
    "stepFailed",
    "stepSkipped",
    "stepPausedByError",
    "stepPausedByOperator",
    "stepCanceled",
    "stepPendingApproval",
    "stepExecutionBehaviorChangedToUngraceful",
    "stepPendingApplicationHealthMonitor",
    "planEvaluationWarning",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "unknown",
        "executionPending",
        "executionStarted",
        "executionSucceeded",
        "executionFailed",
        "executionPausing",
        "executionPaused",
        "executionCanceling",
        "executionCanceled",
        "executionPendingApproval",
        "executionBehaviorChangedToUngraceful",
        "executionBehaviorChangedToGraceful",
        "executionPendingChildPlanManualApproval",
        "executionSuccessMonitoringApplicationHealth",
        "stepStarted",
        "stepUpdate",
        "stepSucceeded",
        "stepFailed",
        "stepSkipped",
        "stepPausedByError",
        "stepPausedByOperator",
        "stepCanceled",
        "stepPendingApproval",
        "stepExecutionBehaviorChangedToUngraceful",
        "stepPendingApplicationHealthMonitor",
        "planEvaluationWarning",
    )
)


def serialize_aws_json_1_0(value: ExecutionEventType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExecutionEventType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionEventType value: {data!r}")
    return cast(ExecutionEventType, data)
