"""Generated from Smithy shape ``com.amazonaws.transfer#CertificateUsageType``."""

from typing import Literal, TypeAlias, cast

CertificateUsageType: TypeAlias = Literal[
    "SIGNING",
    "ENCRYPTION",
    "TLS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateUsageType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CertificateUsageType:
    return cast(CertificateUsageType, data)
