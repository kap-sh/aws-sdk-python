"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationComplianceSeverity``."""

from typing import Literal, TypeAlias, cast

AssociationComplianceSeverity: TypeAlias = Literal[
    "CRITICAL",
    "HIGH",
    "MEDIUM",
    "LOW",
    "UNSPECIFIED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationComplianceSeverity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssociationComplianceSeverity:
    return cast(AssociationComplianceSeverity, data)
