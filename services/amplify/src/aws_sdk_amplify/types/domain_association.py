"""Generated from Smithy shape ``com.amazonaws.amplify#DomainAssociation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplify.types.auto_sub_domain_creation_patterns
    import aws_sdk_amplify.types.auto_sub_domain_iam_role
    import aws_sdk_amplify.types.certificate
    import aws_sdk_amplify.types.certificate_verification_dns_record
    import aws_sdk_amplify.types.domain_association_arn
    import aws_sdk_amplify.types.domain_name
    import aws_sdk_amplify.types.domain_status
    import aws_sdk_amplify.types.enable_auto_sub_domain
    import aws_sdk_amplify.types.status_reason
    import aws_sdk_amplify.types.sub_domains
    import aws_sdk_amplify.types.update_status


class DomainAssociation(TypedDict):
    domain_association_arn: (
        "aws_sdk_amplify.types.domain_association_arn.DomainAssociationArn"
    )
    """<p> The Amazon Resource Name (ARN) for the domain association. </p>"""
    domain_name: "aws_sdk_amplify.types.domain_name.DomainName"
    """<p> The name of the domain. </p>"""
    enable_auto_sub_domain: (
        "aws_sdk_amplify.types.enable_auto_sub_domain.EnableAutoSubDomain"
    )
    """<p> Enables the automated creation of subdomains for branches. </p>"""
    auto_sub_domain_creation_patterns: NotRequired[
        "aws_sdk_amplify.types.auto_sub_domain_creation_patterns.AutoSubDomainCreationPatterns"
    ]
    """<p> Sets branch patterns for automatic subdomain creation. </p>"""
    auto_sub_domain_iam_role: NotRequired[
        "aws_sdk_amplify.types.auto_sub_domain_iam_role.AutoSubDomainIAMRole"
    ]
    """<p> The required AWS Identity and Access Management (IAM) service role for the Amazon Resource Name (ARN) for automatically creating subdomains. </p>"""
    domain_status: "aws_sdk_amplify.types.domain_status.DomainStatus"
    """<p> The current status of the domain association. </p>"""
    update_status: NotRequired["aws_sdk_amplify.types.update_status.UpdateStatus"]
    """<p>The status of the domain update operation that is currently in progress. The following list describes the valid update states.</p> <dl> <dt>REQUESTING_CERTIFICATE</dt> <dd> <p>The certificate is in the process of being updated.</p> </dd> <dt>PENDING_VERIFICATION</dt> <dd> <p>Indicates that an Amplify managed certificate is in the process of being verified. This occurs during the creation of a custom domain or when a custom domain is updated to use a managed certificate.</p> </dd> <dt>IMPORTING_CUSTOM_CERTIFICATE</dt> <dd> <p>Indicates that an Amplify custom certificate is in the process of being imported. This occurs during the creation of a custom domain or when a custom domain is updated to use a custom certificate.</p> </dd> <dt>PENDING_DEPLOYMENT</dt> <dd> <p>Indicates that the subdomain or certificate changes are being propagated.</p> </dd> <dt>AWAITING_APP_CNAME</dt> <dd> <p>Amplify is waiting for CNAME records corresponding to subdomains to be propagated. If your custom domain is on Route 53, Amplify handles this for you automatically. For more information about custom domains, see <a href=\"https://docs.aws.amazon.com/amplify/latest/userguide/custom-domains.html\">Setting up custom domains</a> in the <i>Amplify Hosting User Guide</i>. </p> </dd> <dt>UPDATE_COMPLETE</dt> <dd> <p>The certificate has been associated with a domain.</p> </dd> <dt>UPDATE_FAILED</dt> <dd> <p>The certificate has failed to be provisioned or associated, and there is no existing active certificate to roll back to.</p> </dd> </dl>"""
    status_reason: "aws_sdk_amplify.types.status_reason.StatusReason"
    """<p> Additional information that describes why the domain association is in the current state.</p>"""
    certificate_verification_dns_record: NotRequired[
        "aws_sdk_amplify.types.certificate_verification_dns_record.CertificateVerificationDNSRecord"
    ]
    """<p> The DNS record for certificate verification. </p>"""
    sub_domains: "aws_sdk_amplify.types.sub_domains.SubDomains"
    """<p> The subdomains for the domain association. </p>"""
    certificate: NotRequired["aws_sdk_amplify.types.certificate.Certificate"]
    """<p>Describes the SSL/TLS certificate for the domain association. This can be your own custom certificate or the default certificate that Amplify provisions for you.</p> <p>If you are updating your domain to use a different certificate, <code>certificate</code> points to the new certificate that is being created instead of the current active certificate. Otherwise, <code>certificate</code> points to the current active certificate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainAssociation) -> dict:
    out: dict = {}
    out["domainAssociationArn"] = value["domain_association_arn"]
    out["domainName"] = value["domain_name"]
    out["enableAutoSubDomain"] = value["enable_auto_sub_domain"]
    if "auto_sub_domain_creation_patterns" in value:
        import aws_sdk_amplify.types.auto_sub_domain_creation_patterns

        out["autoSubDomainCreationPatterns"] = (
            aws_sdk_amplify.types.auto_sub_domain_creation_patterns.serialize_json(
                value["auto_sub_domain_creation_patterns"]
            )
        )
    if "auto_sub_domain_iam_role" in value:
        out["autoSubDomainIAMRole"] = value["auto_sub_domain_iam_role"]
    import aws_sdk_amplify.types.domain_status

    out["domainStatus"] = aws_sdk_amplify.types.domain_status.serialize_json(
        value["domain_status"]
    )
    if "update_status" in value:
        import aws_sdk_amplify.types.update_status

        out["updateStatus"] = aws_sdk_amplify.types.update_status.serialize_json(
            value["update_status"]
        )
    out["statusReason"] = value["status_reason"]
    if "certificate_verification_dns_record" in value:
        out["certificateVerificationDNSRecord"] = value[
            "certificate_verification_dns_record"
        ]
    import aws_sdk_amplify.types.sub_domains

    out["subDomains"] = aws_sdk_amplify.types.sub_domains.serialize_json(
        value["sub_domains"]
    )
    if "certificate" in value:
        import aws_sdk_amplify.types.certificate

        out["certificate"] = aws_sdk_amplify.types.certificate.serialize_json(
            value["certificate"]
        )
    return out


def deserialize_json(data: dict) -> DomainAssociation:
    out: DomainAssociation = {}  # type: ignore[typeddict-item]
    if "domainAssociationArn" in data:
        out["domain_association_arn"] = data["domainAssociationArn"]
    else:
        raise DeserializationError("DomainAssociation.domain_association_arn required")
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    else:
        raise DeserializationError("DomainAssociation.domain_name required")
    if "enableAutoSubDomain" in data:
        out["enable_auto_sub_domain"] = data["enableAutoSubDomain"]
    else:
        raise DeserializationError("DomainAssociation.enable_auto_sub_domain required")
    if "autoSubDomainCreationPatterns" in data:
        import aws_sdk_amplify.types.auto_sub_domain_creation_patterns

        out["auto_sub_domain_creation_patterns"] = (
            aws_sdk_amplify.types.auto_sub_domain_creation_patterns.deserialize_json(
                data["autoSubDomainCreationPatterns"]
            )
        )
    if "autoSubDomainIAMRole" in data:
        out["auto_sub_domain_iam_role"] = data["autoSubDomainIAMRole"]
    if "domainStatus" in data:
        import aws_sdk_amplify.types.domain_status

        out["domain_status"] = aws_sdk_amplify.types.domain_status.deserialize_json(
            data["domainStatus"]
        )
    else:
        raise DeserializationError("DomainAssociation.domain_status required")
    if "updateStatus" in data:
        import aws_sdk_amplify.types.update_status

        out["update_status"] = aws_sdk_amplify.types.update_status.deserialize_json(
            data["updateStatus"]
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    else:
        raise DeserializationError("DomainAssociation.status_reason required")
    if "certificateVerificationDNSRecord" in data:
        out["certificate_verification_dns_record"] = data[
            "certificateVerificationDNSRecord"
        ]
    if "subDomains" in data:
        import aws_sdk_amplify.types.sub_domains

        out["sub_domains"] = aws_sdk_amplify.types.sub_domains.deserialize_json(
            data["subDomains"]
        )
    else:
        raise DeserializationError("DomainAssociation.sub_domains required")
    if "certificate" in data:
        import aws_sdk_amplify.types.certificate

        out["certificate"] = aws_sdk_amplify.types.certificate.deserialize_json(
            data["certificate"]
        )
    return out
