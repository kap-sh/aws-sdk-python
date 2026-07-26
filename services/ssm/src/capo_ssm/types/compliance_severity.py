"""Generated from Smithy shape ``com.amazonaws.ssm#ComplianceSeverity``."""

from typing import Literal, TypeAlias, cast

ComplianceSeverity: TypeAlias = Literal[
    "CRITICAL",
    "HIGH",
    "MEDIUM",
    "LOW",
    "INFORMATIONAL",
    "UNSPECIFIED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComplianceSeverity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ComplianceSeverity:
    return cast(ComplianceSeverity, data)
