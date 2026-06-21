"""Generated from Smithy shape ``com.amazonaws.sagemaker#BatchStrategy``."""

from typing import Literal, TypeAlias, cast

BatchStrategy: TypeAlias = Literal[
    "MultiRecord",
    "SingleRecord",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BatchStrategy:
    return cast(BatchStrategy, data)
