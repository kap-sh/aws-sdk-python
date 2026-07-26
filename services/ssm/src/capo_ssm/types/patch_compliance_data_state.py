"""Generated from Smithy shape ``com.amazonaws.ssm#PatchComplianceDataState``."""

from typing import Literal, TypeAlias, cast

PatchComplianceDataState: TypeAlias = Literal[
    "INSTALLED",
    "INSTALLED_OTHER",
    "INSTALLED_PENDING_REBOOT",
    "INSTALLED_REJECTED",
    "MISSING",
    "NOT_APPLICABLE",
    "FAILED",
    "AVAILABLE_SECURITY_UPDATE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatchComplianceDataState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PatchComplianceDataState:
    return cast(PatchComplianceDataState, data)
