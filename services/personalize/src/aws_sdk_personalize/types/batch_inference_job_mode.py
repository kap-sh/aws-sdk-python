"""Generated from Smithy shape ``com.amazonaws.personalize#BatchInferenceJobMode``."""

from typing import Literal, TypeAlias, cast

BatchInferenceJobMode: TypeAlias = Literal[
    "BATCH_INFERENCE",
    "THEME_GENERATION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchInferenceJobMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BatchInferenceJobMode:
    return cast(BatchInferenceJobMode, data)
