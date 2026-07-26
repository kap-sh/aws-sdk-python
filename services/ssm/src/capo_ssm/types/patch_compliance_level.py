"""Generated from Smithy shape ``com.amazonaws.ssm#PatchComplianceLevel``."""

from typing import Literal, TypeAlias, cast

PatchComplianceLevel: TypeAlias = Literal[
    "CRITICAL",
    "HIGH",
    "MEDIUM",
    "LOW",
    "INFORMATIONAL",
    "UNSPECIFIED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatchComplianceLevel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PatchComplianceLevel:
    return cast(PatchComplianceLevel, data)
