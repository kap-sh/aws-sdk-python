"""Generated from Smithy shape ``com.amazonaws.lightsail#CertificateDomainValidationStatus``."""

from typing import Literal, TypeAlias, cast

CertificateDomainValidationStatus: TypeAlias = Literal[
    "PENDING_VALIDATION",
    "FAILED",
    "SUCCESS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateDomainValidationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CertificateDomainValidationStatus:
    return cast(CertificateDomainValidationStatus, data)
