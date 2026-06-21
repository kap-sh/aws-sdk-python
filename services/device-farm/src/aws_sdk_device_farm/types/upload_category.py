"""Generated from Smithy shape ``com.amazonaws.devicefarm#UploadCategory``."""

from typing import Literal, TypeAlias, cast

UploadCategory: TypeAlias = Literal[
    "CURATED",
    "PRIVATE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UploadCategory) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UploadCategory:
    return cast(UploadCategory, data)
