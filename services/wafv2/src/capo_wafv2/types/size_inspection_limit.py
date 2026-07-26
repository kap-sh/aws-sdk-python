"""Generated from Smithy shape ``com.amazonaws.wafv2#SizeInspectionLimit``."""

from typing import Literal, TypeAlias, cast

SizeInspectionLimit: TypeAlias = Literal[
    "KB_16",
    "KB_32",
    "KB_48",
    "KB_64",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SizeInspectionLimit) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SizeInspectionLimit:
    return cast(SizeInspectionLimit, data)
