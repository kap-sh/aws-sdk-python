"""Generated from Smithy shape ``com.amazonaws.ssm#StepExecutionFilterKey``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: StepExecutionFilterKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StepExecutionFilterKey:
    return cast(StepExecutionFilterKey, data)
