"""Generated from Smithy shape ``com.amazonaws.sagemaker#SharingType``."""

from typing import Literal, TypeAlias, cast

SharingType: TypeAlias = Literal[
    "Private",
    "Shared",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SharingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SharingType:
    return cast(SharingType, data)
