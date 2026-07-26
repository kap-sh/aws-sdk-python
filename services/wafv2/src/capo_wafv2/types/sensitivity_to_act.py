"""Generated from Smithy shape ``com.amazonaws.wafv2#SensitivityToAct``."""

from typing import Literal, TypeAlias, cast

SensitivityToAct: TypeAlias = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SensitivityToAct) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SensitivityToAct:
    return cast(SensitivityToAct, data)
