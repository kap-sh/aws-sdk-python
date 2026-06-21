"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelRegistrationMode``."""

from typing import Literal, TypeAlias, cast

ModelRegistrationMode: TypeAlias = Literal[
    "AutoModelRegistrationEnabled",
    "AutoModelRegistrationDisabled",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelRegistrationMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelRegistrationMode:
    return cast(ModelRegistrationMode, data)
