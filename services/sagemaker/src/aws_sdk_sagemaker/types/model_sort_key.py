"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelSortKey``."""

from typing import Literal, TypeAlias, cast

ModelSortKey: TypeAlias = Literal[
    "Name",
    "CreationTime",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelSortKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelSortKey:
    return cast(ModelSortKey, data)
