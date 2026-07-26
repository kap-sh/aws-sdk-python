"""Generated from Smithy shape ``com.amazonaws.frauddetector#ModelSource``."""

from typing import Literal, TypeAlias, cast

ModelSource: TypeAlias = Literal["SAGEMAKER",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelSource) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelSource:
    return cast(ModelSource, data)
