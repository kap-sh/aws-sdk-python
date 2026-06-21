"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceExperimentType``."""

from typing import Literal, TypeAlias, cast

InferenceExperimentType: TypeAlias = Literal["ShadowMode",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceExperimentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InferenceExperimentType:
    return cast(InferenceExperimentType, data)
