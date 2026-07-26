"""Generated from Smithy shape ``com.amazonaws.acm#CertificateExport``."""

from typing import Literal, TypeAlias, cast

CertificateExport: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateExport) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CertificateExport:
    return cast(CertificateExport, data)
