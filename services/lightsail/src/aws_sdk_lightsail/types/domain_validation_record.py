"""Generated from Smithy shape ``com.amazonaws.lightsail#DomainValidationRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.certificate_domain_validation_status
    import aws_sdk_lightsail.types.dns_record_creation_state
    import aws_sdk_lightsail.types.domain_name
    import aws_sdk_lightsail.types.resource_record


class DomainValidationRecord(TypedDict, closed=True):
    domain_name: NotRequired["aws_sdk_lightsail.types.domain_name.DomainName"]
    """<p>The domain name of the certificate validation record. For example, <code>example.com</code> or <code>www.example.com</code>.</p>"""
    resource_record: NotRequired[
        "aws_sdk_lightsail.types.resource_record.ResourceRecord"
    ]
    """<p>An object that describes the DNS records to add to your domain's DNS to validate it for the certificate.</p>"""
    dns_record_creation_state: NotRequired[
        "aws_sdk_lightsail.types.dns_record_creation_state.DnsRecordCreationState"
    ]
    """<p>An object that describes the state of the canonical name (CNAME) records that are automatically added by Lightsail to the DNS of the domain to validate domain ownership.</p>"""
    validation_status: NotRequired[
        "aws_sdk_lightsail.types.certificate_domain_validation_status.CertificateDomainValidationStatus"
    ]
    """<p>The validation status of the record.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainValidationRecord) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    if "resource_record" in value:
        import aws_sdk_lightsail.types.resource_record

        out["resourceRecord"] = (
            aws_sdk_lightsail.types.resource_record.serialize_aws_json_1_1(
                value["resource_record"]
            )
        )
    if "dns_record_creation_state" in value:
        import aws_sdk_lightsail.types.dns_record_creation_state

        out["dnsRecordCreationState"] = (
            aws_sdk_lightsail.types.dns_record_creation_state.serialize_aws_json_1_1(
                value["dns_record_creation_state"]
            )
        )
    if "validation_status" in value:
        import aws_sdk_lightsail.types.certificate_domain_validation_status

        out["validationStatus"] = (
            aws_sdk_lightsail.types.certificate_domain_validation_status.serialize_aws_json_1_1(
                value["validation_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DomainValidationRecord:
    out: DomainValidationRecord = {}  # type: ignore[typeddict-item]
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    if "resourceRecord" in data:
        import aws_sdk_lightsail.types.resource_record

        out["resource_record"] = (
            aws_sdk_lightsail.types.resource_record.deserialize_aws_json_1_1(
                data["resourceRecord"]
            )
        )
    if "dnsRecordCreationState" in data:
        import aws_sdk_lightsail.types.dns_record_creation_state

        out["dns_record_creation_state"] = (
            aws_sdk_lightsail.types.dns_record_creation_state.deserialize_aws_json_1_1(
                data["dnsRecordCreationState"]
            )
        )
    if "validationStatus" in data:
        import aws_sdk_lightsail.types.certificate_domain_validation_status

        out["validation_status"] = (
            aws_sdk_lightsail.types.certificate_domain_validation_status.deserialize_aws_json_1_1(
                data["validationStatus"]
            )
        )
    return out
