"""Generated from Smithy shape ``com.amazonaws.lightsail#CertificateProvider``."""

from typing import Literal, TypeAlias, cast

CertificateProvider: TypeAlias = Literal["LetsEncrypt",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateProvider) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CertificateProvider:
    return cast(CertificateProvider, data)
