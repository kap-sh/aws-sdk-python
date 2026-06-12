"""Generated from Smithy shape ``com.amazonaws.iot#ServerCertificateArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.acm_certificate_arn

ServerCertificateArns: TypeAlias = list[
    "aws_sdk_iot.types.acm_certificate_arn.AcmCertificateArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServerCertificateArns) -> list:
    return list(value)


def deserialize_json(data: list) -> ServerCertificateArns:
    return list(data)
