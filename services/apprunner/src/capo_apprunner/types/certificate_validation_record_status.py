"""Generated from Smithy shape ``com.amazonaws.apprunner#CertificateValidationRecordStatus``."""

from typing import Literal, TypeAlias, cast

CertificateValidationRecordStatus: TypeAlias = Literal[
    "PENDING_VALIDATION",
    "SUCCESS",
    "FAILED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CertificateValidationRecordStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CertificateValidationRecordStatus:
    return cast(CertificateValidationRecordStatus, data)
