"""Generated from Smithy shape ``com.amazonaws.sagemaker#TagPropagation``."""

from typing import Literal, TypeAlias, cast

TagPropagation: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagPropagation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TagPropagation:
    return cast(TagPropagation, data)
