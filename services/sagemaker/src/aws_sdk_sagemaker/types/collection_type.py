"""Generated from Smithy shape ``com.amazonaws.sagemaker#CollectionType``."""

from typing import Literal, TypeAlias, cast

CollectionType: TypeAlias = Literal[
    "List",
    "Set",
    "Vector",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CollectionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CollectionType:
    return cast(CollectionType, data)
