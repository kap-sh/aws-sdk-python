"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelVariantAction``."""

from typing import Literal, TypeAlias, cast

ModelVariantAction: TypeAlias = Literal[
    "Retain",
    "Remove",
    "Promote",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelVariantAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelVariantAction:
    return cast(ModelVariantAction, data)
