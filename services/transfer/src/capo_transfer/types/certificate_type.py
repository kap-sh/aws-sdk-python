"""Generated from Smithy shape ``com.amazonaws.transfer#CertificateType``."""

from typing import Literal, TypeAlias, cast

CertificateType: TypeAlias = Literal[
    "CERTIFICATE",
    "CERTIFICATE_WITH_PRIVATE_KEY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CertificateType:
    return cast(CertificateType, data)
