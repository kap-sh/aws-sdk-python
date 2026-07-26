"""Generated from Smithy shape ``com.amazonaws.lightsail#LoadBalancerTlsCertificateDomainValidationRecordList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.load_balancer_tls_certificate_domain_validation_record

LoadBalancerTlsCertificateDomainValidationRecordList: TypeAlias = list[
    "capo_lightsail.types.load_balancer_tls_certificate_domain_validation_record.LoadBalancerTlsCertificateDomainValidationRecord"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: LoadBalancerTlsCertificateDomainValidationRecordList,
) -> list:
    import capo_lightsail.types.load_balancer_tls_certificate_domain_validation_record

    out: list = []
    for item in value:
        out.append(
            capo_lightsail.types.load_balancer_tls_certificate_domain_validation_record.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: list,
) -> LoadBalancerTlsCertificateDomainValidationRecordList:
    import capo_lightsail.types.load_balancer_tls_certificate_domain_validation_record

    out: LoadBalancerTlsCertificateDomainValidationRecordList = []
    for item in data:
        out.append(
            capo_lightsail.types.load_balancer_tls_certificate_domain_validation_record.deserialize_aws_json_1_1(
                item
            )
        )
    return out
