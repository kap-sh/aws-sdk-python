"""Generated from Smithy shape ``com.amazonaws.lightsail#LoadBalancerTlsCertificateDomainValidationOption``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.domain_name
    import aws_sdk_lightsail.types.load_balancer_tls_certificate_domain_status


class LoadBalancerTlsCertificateDomainValidationOption(TypedDict):
    domain_name: NotRequired["aws_sdk_lightsail.types.domain_name.DomainName"]
    """<p>The fully qualified domain name in the certificate request.</p>"""
    validation_status: NotRequired[
        "aws_sdk_lightsail.types.load_balancer_tls_certificate_domain_status.LoadBalancerTlsCertificateDomainStatus"
    ]
    """<p>The status of the domain validation. Valid values are listed below.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: LoadBalancerTlsCertificateDomainValidationOption,
) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    if "validation_status" in value:
        import aws_sdk_lightsail.types.load_balancer_tls_certificate_domain_status

        out["validationStatus"] = (
            aws_sdk_lightsail.types.load_balancer_tls_certificate_domain_status.serialize_aws_json_1_1(
                value["validation_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> LoadBalancerTlsCertificateDomainValidationOption:
    out: LoadBalancerTlsCertificateDomainValidationOption = {}  # type: ignore[typeddict-item]
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    if "validationStatus" in data:
        import aws_sdk_lightsail.types.load_balancer_tls_certificate_domain_status

        out["validation_status"] = (
            aws_sdk_lightsail.types.load_balancer_tls_certificate_domain_status.deserialize_aws_json_1_1(
                data["validationStatus"]
            )
        )
    return out
