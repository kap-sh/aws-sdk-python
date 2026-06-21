"""Generated from Smithy shape ``com.amazonaws.ssm#PatchComplianceStatus``."""

from typing import Literal, TypeAlias, cast

PatchComplianceStatus: TypeAlias = Literal[
    "COMPLIANT",
    "NON_COMPLIANT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatchComplianceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PatchComplianceStatus:
    return cast(PatchComplianceStatus, data)
