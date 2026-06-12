"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCertificateManagerCertificateKeyUsages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_certificate_manager_certificate_key_usage

AwsCertificateManagerCertificateKeyUsages: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_certificate_manager_certificate_key_usage.AwsCertificateManagerCertificateKeyUsage"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsCertificateManagerCertificateKeyUsages) -> list:
    import aws_sdk_securityhub.types.aws_certificate_manager_certificate_key_usage

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_certificate_manager_certificate_key_usage.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsCertificateManagerCertificateKeyUsages:
    import aws_sdk_securityhub.types.aws_certificate_manager_certificate_key_usage

    out: AwsCertificateManagerCertificateKeyUsages = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_certificate_manager_certificate_key_usage.deserialize_json(
                item
            )
        )
    return out
