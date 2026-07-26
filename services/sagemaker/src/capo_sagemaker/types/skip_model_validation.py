"""Generated from Smithy shape ``com.amazonaws.sagemaker#SkipModelValidation``."""

from typing import Literal, TypeAlias, cast

SkipModelValidation: TypeAlias = Literal[
    "All",
    "None",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SkipModelValidation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SkipModelValidation:
    return cast(SkipModelValidation, data)
