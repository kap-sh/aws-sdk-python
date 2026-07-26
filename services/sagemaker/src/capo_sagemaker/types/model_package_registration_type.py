"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelPackageRegistrationType``."""

from typing import Literal, TypeAlias, cast

ModelPackageRegistrationType: TypeAlias = Literal[
    "Logged",
    "Registered",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelPackageRegistrationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelPackageRegistrationType:
    return cast(ModelPackageRegistrationType, data)
