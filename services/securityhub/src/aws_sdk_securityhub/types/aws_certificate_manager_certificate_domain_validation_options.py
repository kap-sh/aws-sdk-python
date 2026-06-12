"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCertificateManagerCertificateDomainValidationOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_certificate_manager_certificate_domain_validation_option

AwsCertificateManagerCertificateDomainValidationOptions: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_certificate_manager_certificate_domain_validation_option.AwsCertificateManagerCertificateDomainValidationOption"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsCertificateManagerCertificateDomainValidationOptions,
) -> list:
    import aws_sdk_securityhub.types.aws_certificate_manager_certificate_domain_validation_option

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_certificate_manager_certificate_domain_validation_option.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AwsCertificateManagerCertificateDomainValidationOptions:
    import aws_sdk_securityhub.types.aws_certificate_manager_certificate_domain_validation_option

    out: AwsCertificateManagerCertificateDomainValidationOptions = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_certificate_manager_certificate_domain_validation_option.deserialize_json(
                item
            )
        )
    return out
