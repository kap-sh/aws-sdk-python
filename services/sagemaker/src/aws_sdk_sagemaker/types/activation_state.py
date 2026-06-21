"""Generated from Smithy shape ``com.amazonaws.sagemaker#ActivationState``."""

from typing import Literal, TypeAlias, cast

ActivationState: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActivationState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ActivationState:
    return cast(ActivationState, data)
