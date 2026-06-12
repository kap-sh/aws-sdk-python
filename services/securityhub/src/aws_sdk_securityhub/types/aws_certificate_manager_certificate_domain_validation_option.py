"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCertificateManagerCertificateDomainValidationOption``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_certificate_manager_certificate_resource_record
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.string_list


class AwsCertificateManagerCertificateDomainValidationOption(TypedDict):
    domain_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>A fully qualified domain name (FQDN) in the certificate.</p>"""
    resource_record: NotRequired[
        "aws_sdk_securityhub.types.aws_certificate_manager_certificate_resource_record.AwsCertificateManagerCertificateResourceRecord"
    ]
    """<p>The CNAME record that is added to the DNS database for domain validation.</p>"""
    validation_domain: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The domain name that Certificate Manager uses to send domain validation emails.</p>"""
    validation_emails: NotRequired["aws_sdk_securityhub.types.string_list.StringList"]
    """<p>A list of email addresses that Certificate Manager uses to send domain validation emails.</p>"""
    validation_method: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The method used to validate the domain name.</p>"""
    validation_status: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The validation status of the domain name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsCertificateManagerCertificateDomainValidationOption,
) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "resource_record" in value:
        import aws_sdk_securityhub.types.aws_certificate_manager_certificate_resource_record

        out["ResourceRecord"] = (
            aws_sdk_securityhub.types.aws_certificate_manager_certificate_resource_record.serialize_json(
                value["resource_record"]
            )
        )
    if "validation_domain" in value:
        out["ValidationDomain"] = value["validation_domain"]
    if "validation_emails" in value:
        import aws_sdk_securityhub.types.string_list

        out["ValidationEmails"] = aws_sdk_securityhub.types.string_list.serialize_json(
            value["validation_emails"]
        )
    if "validation_method" in value:
        out["ValidationMethod"] = value["validation_method"]
    if "validation_status" in value:
        out["ValidationStatus"] = value["validation_status"]
    return out


def deserialize_json(
    data: dict,
) -> AwsCertificateManagerCertificateDomainValidationOption:
    out: AwsCertificateManagerCertificateDomainValidationOption = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    if "ResourceRecord" in data:
        import aws_sdk_securityhub.types.aws_certificate_manager_certificate_resource_record

        out["resource_record"] = (
            aws_sdk_securityhub.types.aws_certificate_manager_certificate_resource_record.deserialize_json(
                data["ResourceRecord"]
            )
        )
    if "ValidationDomain" in data:
        out["validation_domain"] = data["ValidationDomain"]
    if "ValidationEmails" in data:
        import aws_sdk_securityhub.types.string_list

        out["validation_emails"] = (
            aws_sdk_securityhub.types.string_list.deserialize_json(
                data["ValidationEmails"]
            )
        )
    if "ValidationMethod" in data:
        out["validation_method"] = data["ValidationMethod"]
    if "ValidationStatus" in data:
        out["validation_status"] = data["ValidationStatus"]
    return out
