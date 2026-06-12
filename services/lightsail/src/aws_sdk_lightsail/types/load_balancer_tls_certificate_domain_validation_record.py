"""Generated from Smithy shape ``com.amazonaws.lightsail#LoadBalancerTlsCertificateDomainValidationRecord``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.domain_name
    import aws_sdk_lightsail.types.load_balancer_tls_certificate_dns_record_creation_state
    import aws_sdk_lightsail.types.load_balancer_tls_certificate_domain_status
    import aws_sdk_lightsail.types.non_empty_string


class LoadBalancerTlsCertificateDomainValidationRecord(TypedDict):
    name: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>A fully qualified domain name in the certificate. For example, <code>example.com</code>.</p>"""
    type: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The type of validation record. For example, <code>CNAME</code> for domain validation.</p>"""
    value: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The value for that type.</p>"""
    validation_status: NotRequired[
        "aws_sdk_lightsail.types.load_balancer_tls_certificate_domain_status.LoadBalancerTlsCertificateDomainStatus"
    ]
    """<p>The validation status. Valid values are listed below.</p>"""
    domain_name: NotRequired["aws_sdk_lightsail.types.domain_name.DomainName"]
    """<p>The domain name against which your SSL/TLS certificate was validated.</p>"""
    dns_record_creation_state: NotRequired[
        "aws_sdk_lightsail.types.load_balancer_tls_certificate_dns_record_creation_state.LoadBalancerTlsCertificateDnsRecordCreationState"
    ]
    """<p>An object that describes the state of the canonical name (CNAME) records that are automatically added by Lightsail to the DNS of a domain to validate domain ownership.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: LoadBalancerTlsCertificateDomainValidationRecord,
) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        out["type"] = value["type"]
    if "value" in value:
        out["value"] = value["value"]
    if "validation_status" in value:
        import aws_sdk_lightsail.types.load_balancer_tls_certificate_domain_status

        out["validationStatus"] = (
            aws_sdk_lightsail.types.load_balancer_tls_certificate_domain_status.serialize_aws_json_1_1(
                value["validation_status"]
            )
        )
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    if "dns_record_creation_state" in value:
        import aws_sdk_lightsail.types.load_balancer_tls_certificate_dns_record_creation_state

        out["dnsRecordCreationState"] = (
            aws_sdk_lightsail.types.load_balancer_tls_certificate_dns_record_creation_state.serialize_aws_json_1_1(
                value["dns_record_creation_state"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> LoadBalancerTlsCertificateDomainValidationRecord:
    out: LoadBalancerTlsCertificateDomainValidationRecord = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "type" in data:
        out["type"] = data["type"]
    if "value" in data:
        out["value"] = data["value"]
    if "validationStatus" in data:
        import aws_sdk_lightsail.types.load_balancer_tls_certificate_domain_status

        out["validation_status"] = (
            aws_sdk_lightsail.types.load_balancer_tls_certificate_domain_status.deserialize_aws_json_1_1(
                data["validationStatus"]
            )
        )
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    if "dnsRecordCreationState" in data:
        import aws_sdk_lightsail.types.load_balancer_tls_certificate_dns_record_creation_state

        out["dns_record_creation_state"] = (
            aws_sdk_lightsail.types.load_balancer_tls_certificate_dns_record_creation_state.deserialize_aws_json_1_1(
                data["dnsRecordCreationState"]
            )
        )
    return out
