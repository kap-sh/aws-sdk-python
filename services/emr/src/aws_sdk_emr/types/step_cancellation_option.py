"""Generated from Smithy shape ``com.amazonaws.emr#StepCancellationOption``."""

from typing import Literal, TypeAlias, cast

StepCancellationOption: TypeAlias = Literal[
    "SEND_INTERRUPT",
    "TERMINATE_PROCESS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StepCancellationOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StepCancellationOption:
    return cast(StepCancellationOption, data)
