"""Generated from Smithy shape ``com.amazonaws.lightsail#LoadBalancerTlsCertificateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.load_balancer_tls_certificate

LoadBalancerTlsCertificateList: TypeAlias = list[
    "capo_lightsail.types.load_balancer_tls_certificate.LoadBalancerTlsCertificate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoadBalancerTlsCertificateList) -> list:
    import capo_lightsail.types.load_balancer_tls_certificate

    out: list = []
    for item in value:
        out.append(
            capo_lightsail.types.load_balancer_tls_certificate.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LoadBalancerTlsCertificateList:
    import capo_lightsail.types.load_balancer_tls_certificate

    out: LoadBalancerTlsCertificateList = []
    for item in data:
        out.append(
            capo_lightsail.types.load_balancer_tls_certificate.deserialize_aws_json_1_1(
                item
            )
        )
    return out
