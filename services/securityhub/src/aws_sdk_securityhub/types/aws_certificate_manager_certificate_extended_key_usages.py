"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCertificateManagerCertificateExtendedKeyUsages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_certificate_manager_certificate_extended_key_usage

AwsCertificateManagerCertificateExtendedKeyUsages: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_certificate_manager_certificate_extended_key_usage.AwsCertificateManagerCertificateExtendedKeyUsage"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsCertificateManagerCertificateExtendedKeyUsages) -> list:
    import aws_sdk_securityhub.types.aws_certificate_manager_certificate_extended_key_usage

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_certificate_manager_certificate_extended_key_usage.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsCertificateManagerCertificateExtendedKeyUsages:
    import aws_sdk_securityhub.types.aws_certificate_manager_certificate_extended_key_usage

    out: AwsCertificateManagerCertificateExtendedKeyUsages = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_certificate_manager_certificate_extended_key_usage.deserialize_json(
                item
            )
        )
    return out
