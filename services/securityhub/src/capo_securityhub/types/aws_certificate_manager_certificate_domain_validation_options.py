"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCertificateManagerCertificateDomainValidationOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_certificate_manager_certificate_domain_validation_option

AwsCertificateManagerCertificateDomainValidationOptions: TypeAlias = list[
    "capo_securityhub.types.aws_certificate_manager_certificate_domain_validation_option.AwsCertificateManagerCertificateDomainValidationOption"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsCertificateManagerCertificateDomainValidationOptions,
) -> list:
    import capo_securityhub.types.aws_certificate_manager_certificate_domain_validation_option

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_certificate_manager_certificate_domain_validation_option.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AwsCertificateManagerCertificateDomainValidationOptions:
    import capo_securityhub.types.aws_certificate_manager_certificate_domain_validation_option

    out: AwsCertificateManagerCertificateDomainValidationOptions = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_certificate_manager_certificate_domain_validation_option.deserialize_json(
                item
            )
        )
    return out
