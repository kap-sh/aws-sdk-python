"""Generated from Smithy shape ``com.amazonaws.ssm#PlatformType``."""

from typing import Literal, TypeAlias, cast

PlatformType: TypeAlias = Literal[
    "Windows",
    "Linux",
    "MacOS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlatformType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PlatformType:
    return cast(PlatformType, data)
