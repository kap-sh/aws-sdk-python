"""Generated from Smithy shape ``com.amazonaws.acmpca#CertificateAuthorityType``."""

from typing import Literal, TypeAlias, cast

CertificateAuthorityType: TypeAlias = Literal[
    "ROOT",
    "SUBORDINATE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateAuthorityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CertificateAuthorityType:
    return cast(CertificateAuthorityType, data)
