"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceComponentSortKey``."""

from typing import Literal, TypeAlias, cast

InferenceComponentSortKey: TypeAlias = Literal[
    "Name",
    "CreationTime",
    "Status",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceComponentSortKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InferenceComponentSortKey:
    return cast(InferenceComponentSortKey, data)
