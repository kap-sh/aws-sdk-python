"""Generated from Smithy shape ``com.amazonaws.acm#CertificateStatus``."""

from typing import Literal, TypeAlias, cast

CertificateStatus: TypeAlias = Literal[
    "PENDING_VALIDATION",
    "ISSUED",
    "INACTIVE",
    "EXPIRED",
    "VALIDATION_TIMED_OUT",
    "REVOKED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CertificateStatus:
    return cast(CertificateStatus, data)
