"""Generated from Smithy shape ``com.amazonaws.lightsail#LoadBalancerTlsCertificateDomainValidationOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.load_balancer_tls_certificate_domain_validation_option

LoadBalancerTlsCertificateDomainValidationOptionList: TypeAlias = list[
    "capo_lightsail.types.load_balancer_tls_certificate_domain_validation_option.LoadBalancerTlsCertificateDomainValidationOption"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: LoadBalancerTlsCertificateDomainValidationOptionList,
) -> list:
    import capo_lightsail.types.load_balancer_tls_certificate_domain_validation_option

    out: list = []
    for item in value:
        out.append(
            capo_lightsail.types.load_balancer_tls_certificate_domain_validation_option.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: list,
) -> LoadBalancerTlsCertificateDomainValidationOptionList:
    import capo_lightsail.types.load_balancer_tls_certificate_domain_validation_option

    out: LoadBalancerTlsCertificateDomainValidationOptionList = []
    for item in data:
        out.append(
            capo_lightsail.types.load_balancer_tls_certificate_domain_validation_option.deserialize_aws_json_1_1(
                item
            )
        )
    return out
