"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceComponentStatus``."""

from typing import Literal, TypeAlias, cast

InferenceComponentStatus: TypeAlias = Literal[
    "InService",
    "Creating",
    "Updating",
    "Failed",
    "Deleting",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceComponentStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InferenceComponentStatus:
    return cast(InferenceComponentStatus, data)
