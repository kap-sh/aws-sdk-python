"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#StepStatus``."""

from typing import Literal, TypeAlias, cast

StepStatus: TypeAlias = Literal[
    "Ready",
    "InProgress",
    "Complete",
    "Failed",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StepStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StepStatus:
    return cast(StepStatus, data)
