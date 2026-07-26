"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelVariantStatus``."""

from typing import Literal, TypeAlias, cast

ModelVariantStatus: TypeAlias = Literal[
    "Creating",
    "Updating",
    "InService",
    "Deleting",
    "Deleted",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelVariantStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelVariantStatus:
    return cast(ModelVariantStatus, data)
