"""Generated from Smithy shape ``com.amazonaws.wafv2#SensitivityLevel``."""

from typing import Literal, TypeAlias, cast

SensitivityLevel: TypeAlias = Literal[
    "LOW",
    "HIGH",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SensitivityLevel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SensitivityLevel:
    return cast(SensitivityLevel, data)
