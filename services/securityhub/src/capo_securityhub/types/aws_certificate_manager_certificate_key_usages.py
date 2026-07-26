"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCertificateManagerCertificateKeyUsages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_certificate_manager_certificate_key_usage

AwsCertificateManagerCertificateKeyUsages: TypeAlias = list[
    "capo_securityhub.types.aws_certificate_manager_certificate_key_usage.AwsCertificateManagerCertificateKeyUsage"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsCertificateManagerCertificateKeyUsages) -> list:
    import capo_securityhub.types.aws_certificate_manager_certificate_key_usage

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_certificate_manager_certificate_key_usage.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsCertificateManagerCertificateKeyUsages:
    import capo_securityhub.types.aws_certificate_manager_certificate_key_usage

    out: AwsCertificateManagerCertificateKeyUsages = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_certificate_manager_certificate_key_usage.deserialize_json(
                item
            )
        )
    return out
