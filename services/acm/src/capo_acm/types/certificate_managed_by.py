"""Generated from Smithy shape ``com.amazonaws.acm#CertificateManagedBy``."""

from typing import Literal, TypeAlias, cast

CertificateManagedBy: TypeAlias = Literal["CLOUDFRONT",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateManagedBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CertificateManagedBy:
    return cast(CertificateManagedBy, data)
