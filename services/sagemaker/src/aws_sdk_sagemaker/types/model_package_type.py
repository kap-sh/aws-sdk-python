"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelPackageType``."""

from typing import Literal, TypeAlias, cast

ModelPackageType: TypeAlias = Literal[
    "Versioned",
    "Unversioned",
    "Both",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelPackageType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelPackageType:
    return cast(ModelPackageType, data)
