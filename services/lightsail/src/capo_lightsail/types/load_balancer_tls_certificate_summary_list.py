"""Generated from Smithy shape ``com.amazonaws.lightsail#LoadBalancerTlsCertificateSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.load_balancer_tls_certificate_summary

LoadBalancerTlsCertificateSummaryList: TypeAlias = list[
    "capo_lightsail.types.load_balancer_tls_certificate_summary.LoadBalancerTlsCertificateSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoadBalancerTlsCertificateSummaryList) -> list:
    import capo_lightsail.types.load_balancer_tls_certificate_summary

    out: list = []
    for item in value:
        out.append(
            capo_lightsail.types.load_balancer_tls_certificate_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LoadBalancerTlsCertificateSummaryList:
    import capo_lightsail.types.load_balancer_tls_certificate_summary

    out: LoadBalancerTlsCertificateSummaryList = []
    for item in data:
        out.append(
            capo_lightsail.types.load_balancer_tls_certificate_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
