"""Generated from Smithy shape ``com.amazonaws.transfer#CertificateStatusType``."""

from typing import Literal, TypeAlias, cast

CertificateStatusType: TypeAlias = Literal[
    "ACTIVE",
    "PENDING_ROTATION",
    "INACTIVE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateStatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CertificateStatusType:
    return cast(CertificateStatusType, data)
