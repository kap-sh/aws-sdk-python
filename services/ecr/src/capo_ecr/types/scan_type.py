"""Generated from Smithy shape ``com.amazonaws.ecr#ScanType``."""

from typing import Literal, TypeAlias, cast

ScanType: TypeAlias = Literal[
    "BASIC",
    "ENHANCED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScanType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScanType:
    return cast(ScanType, data)
