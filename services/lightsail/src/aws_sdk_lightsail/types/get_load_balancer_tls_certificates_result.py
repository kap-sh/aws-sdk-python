"""Generated from Smithy shape ``com.amazonaws.lightsail#GetLoadBalancerTlsCertificatesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.load_balancer_tls_certificate_list


class GetLoadBalancerTlsCertificatesResult(TypedDict, closed=True):
    tls_certificates: NotRequired[
        "aws_sdk_lightsail.types.load_balancer_tls_certificate_list.LoadBalancerTlsCertificateList"
    ]
    """<p>An array of LoadBalancerTlsCertificate objects describing your SSL/TLS certificates.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLoadBalancerTlsCertificatesResult) -> dict:
    out: dict = {}
    if "tls_certificates" in value:
        import aws_sdk_lightsail.types.load_balancer_tls_certificate_list

        out["tlsCertificates"] = (
            aws_sdk_lightsail.types.load_balancer_tls_certificate_list.serialize_aws_json_1_1(
                value["tls_certificates"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLoadBalancerTlsCertificatesResult:
    out: GetLoadBalancerTlsCertificatesResult = {}  # type: ignore[typeddict-item]
    if "tlsCertificates" in data:
        import aws_sdk_lightsail.types.load_balancer_tls_certificate_list

        out["tls_certificates"] = (
            aws_sdk_lightsail.types.load_balancer_tls_certificate_list.deserialize_aws_json_1_1(
                data["tlsCertificates"]
            )
        )
    return out
