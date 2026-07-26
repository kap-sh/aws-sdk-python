"""Generated from Smithy shape ``com.amazonaws.acm#CertificateTransparencyLoggingPreference``."""

from typing import Literal, TypeAlias, cast

CertificateTransparencyLoggingPreference: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateTransparencyLoggingPreference) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CertificateTransparencyLoggingPreference:
    return cast(CertificateTransparencyLoggingPreference, data)
