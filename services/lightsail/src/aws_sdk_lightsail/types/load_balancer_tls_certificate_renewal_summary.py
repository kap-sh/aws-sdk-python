"""Generated from Smithy shape ``com.amazonaws.lightsail#LoadBalancerTlsCertificateRenewalSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.load_balancer_tls_certificate_domain_validation_option_list
    import aws_sdk_lightsail.types.load_balancer_tls_certificate_renewal_status


class LoadBalancerTlsCertificateRenewalSummary(TypedDict, closed=True):
    renewal_status: NotRequired[
        "aws_sdk_lightsail.types.load_balancer_tls_certificate_renewal_status.LoadBalancerTlsCertificateRenewalStatus"
    ]
    """<p>The renewal status of the certificate.</p> <p>The following renewal status are possible:</p> <ul> <li> <p> <b> <code>PendingAutoRenewal</code> </b> - Lightsail is attempting to automatically validate the domain names of the certificate. No further action is required. </p> </li> <li> <p> <b> <code>PendingValidation</code> </b> - Lightsail couldn't automatically validate one or more domain names of the certificate. You must take action to validate these domain names or the certificate won't be renewed. Check to make sure your certificate's domain validation records exist in your domain's DNS, and that your certificate remains in use.</p> </li> <li> <p> <b> <code>Success</code> </b> - All domain names in the certificate are validated, and Lightsail renewed the certificate. No further action is required. </p> </li> <li> <p> <b> <code>Failed</code> </b> - One or more domain names were not validated before the certificate expired, and Lightsail did not renew the certificate. You can request a new certificate using the <code>CreateCertificate</code> action.</p> </li> </ul>"""
    domain_validation_options: NotRequired[
        "aws_sdk_lightsail.types.load_balancer_tls_certificate_domain_validation_option_list.LoadBalancerTlsCertificateDomainValidationOptionList"
    ]
    """<p>Contains information about the validation of each domain name in the certificate, as it pertains to Lightsail's managed renewal. This is different from the initial validation that occurs as a result of the RequestCertificate request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoadBalancerTlsCertificateRenewalSummary) -> dict:
    out: dict = {}
    if "renewal_status" in value:
        import aws_sdk_lightsail.types.load_balancer_tls_certificate_renewal_status

        out["renewalStatus"] = (
            aws_sdk_lightsail.types.load_balancer_tls_certificate_renewal_status.serialize_aws_json_1_1(
                value["renewal_status"]
            )
        )
    if "domain_validation_options" in value:
        import aws_sdk_lightsail.types.load_balancer_tls_certificate_domain_validation_option_list

        out["domainValidationOptions"] = (
            aws_sdk_lightsail.types.load_balancer_tls_certificate_domain_validation_option_list.serialize_aws_json_1_1(
                value["domain_validation_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LoadBalancerTlsCertificateRenewalSummary:
    out: LoadBalancerTlsCertificateRenewalSummary = {}  # type: ignore[typeddict-item]
    if "renewalStatus" in data:
        import aws_sdk_lightsail.types.load_balancer_tls_certificate_renewal_status

        out["renewal_status"] = (
            aws_sdk_lightsail.types.load_balancer_tls_certificate_renewal_status.deserialize_aws_json_1_1(
                data["renewalStatus"]
            )
        )
    if "domainValidationOptions" in data:
        import aws_sdk_lightsail.types.load_balancer_tls_certificate_domain_validation_option_list

        out["domain_validation_options"] = (
            aws_sdk_lightsail.types.load_balancer_tls_certificate_domain_validation_option_list.deserialize_aws_json_1_1(
                data["domainValidationOptions"]
            )
        )
    return out
