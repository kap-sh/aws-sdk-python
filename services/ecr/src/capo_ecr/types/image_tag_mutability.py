"""Generated from Smithy shape ``com.amazonaws.ecr#ImageTagMutability``."""

from typing import Literal, TypeAlias, cast

ImageTagMutability: TypeAlias = Literal[
    "MUTABLE",
    "IMMUTABLE",
    "IMMUTABLE_WITH_EXCLUSION",
    "MUTABLE_WITH_EXCLUSION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageTagMutability) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImageTagMutability:
    return cast(ImageTagMutability, data)
