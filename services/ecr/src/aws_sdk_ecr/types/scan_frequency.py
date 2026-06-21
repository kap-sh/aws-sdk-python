"""Generated from Smithy shape ``com.amazonaws.ecr#ScanFrequency``."""

from typing import Literal, TypeAlias, cast

ScanFrequency: TypeAlias = Literal[
    "SCAN_ON_PUSH",
    "CONTINUOUS_SCAN",
    "MANUAL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScanFrequency) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScanFrequency:
    return cast(ScanFrequency, data)
