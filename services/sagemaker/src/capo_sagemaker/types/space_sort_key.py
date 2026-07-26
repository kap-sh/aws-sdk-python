"""Generated from Smithy shape ``com.amazonaws.sagemaker#SpaceSortKey``."""

from typing import Literal, TypeAlias, cast

SpaceSortKey: TypeAlias = Literal[
    "CreationTime",
    "LastModifiedTime",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SpaceSortKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SpaceSortKey:
    return cast(SpaceSortKey, data)
