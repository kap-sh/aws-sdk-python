"""Generated from Smithy shape ``com.amazonaws.ssm#StepExecutionFilterKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

StepExecutionFilterKey: TypeAlias = Literal[
    "StartTimeBefore",
    "StartTimeAfter",
    "StepExecutionStatus",
    "StepExecutionId",
    "StepName",
    "Action",
    "ParentStepExecutionId",
    "ParentStepIteration",
    "ParentStepIteratorValue",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "StartTimeBefore",
        "StartTimeAfter",
        "StepExecutionStatus",
        "StepExecutionId",
        "StepName",
        "Action",
        "ParentStepExecutionId",
        "ParentStepIteration",
        "ParentStepIteratorValue",
    )
)


def serialize_aws_json_1_1(value: StepExecutionFilterKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StepExecutionFilterKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StepExecutionFilterKey value: {data!r}")
    return cast(StepExecutionFilterKey, data)
