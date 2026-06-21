"""Generated from Smithy shape ``com.amazonaws.ssm#ComplianceStatus``."""

from typing import Literal, TypeAlias, cast

ComplianceStatus: TypeAlias = Literal[
    "COMPLIANT",
    "NON_COMPLIANT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComplianceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ComplianceStatus:
    return cast(ComplianceStatus, data)
