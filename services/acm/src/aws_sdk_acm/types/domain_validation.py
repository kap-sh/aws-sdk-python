"""Generated from Smithy shape ``com.amazonaws.acm#DomainValidation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_acm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_acm.types.domain_name_string
    import aws_sdk_acm.types.domain_status
    import aws_sdk_acm.types.http_redirect
    import aws_sdk_acm.types.resource_record
    import aws_sdk_acm.types.validation_email_list
    import aws_sdk_acm.types.validation_method


class DomainValidation(TypedDict, closed=True):
    domain_name: "aws_sdk_acm.types.domain_name_string.DomainNameString"
    """<p>A fully qualified domain name (FQDN) in the certificate. For example, <code>www.example.com</code> or <code>example.com</code>. </p>"""
    validation_emails: NotRequired[
        "aws_sdk_acm.types.validation_email_list.ValidationEmailList"
    ]
    """<p>A list of email addresses that ACM used to send domain validation emails.</p>"""
    validation_domain: NotRequired[
        "aws_sdk_acm.types.domain_name_string.DomainNameString"
    ]
    """<p>The domain name that ACM used to send domain validation emails.</p>"""
    validation_status: NotRequired["aws_sdk_acm.types.domain_status.DomainStatus"]
    """<p>The validation status of the domain name. This can be one of the following values:</p> <ul> <li> <p> <code>PENDING_VALIDATION</code> </p> </li> <li> <p> <code/>SUCCESS</p> </li> <li> <p> <code/>FAILED</p> </li> </ul>"""
    resource_record: NotRequired["aws_sdk_acm.types.resource_record.ResourceRecord"]
    r"""<p>Contains the CNAME record that you add to your DNS database for domain validation. For more information, see <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-dns.html\">Use DNS to Validate Domain Ownership</a>.</p> <note> <p>The CNAME information that you need does not include the name of your domain. If you include your domain name in the DNS database CNAME record, validation fails. For example, if the name is <code>_a79865eb4cd1a6ab990a45779b4e0b96.yourdomain.com</code>, only <code>_a79865eb4cd1a6ab990a45779b4e0b96</code> must be used.</p> </note>"""
    http_redirect: NotRequired["aws_sdk_acm.types.http_redirect.HttpRedirect"]
    """<p>Contains information for HTTP-based domain validation of certificates requested through Amazon CloudFront and issued by ACM. This field exists only when the certificate type is <code>AMAZON_ISSUED</code> and the validation method is <code>HTTP</code>.</p>"""
    validation_method: NotRequired[
        "aws_sdk_acm.types.validation_method.ValidationMethod"
    ]
    """<p>Specifies the domain validation method.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainValidation) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    if "validation_emails" in value:
        import aws_sdk_acm.types.validation_email_list

        out["ValidationEmails"] = (
            aws_sdk_acm.types.validation_email_list.serialize_aws_json_1_1(
                value["validation_emails"]
            )
        )
    if "validation_domain" in value:
        out["ValidationDomain"] = value["validation_domain"]
    if "validation_status" in value:
        import aws_sdk_acm.types.domain_status

        out["ValidationStatus"] = (
            aws_sdk_acm.types.domain_status.serialize_aws_json_1_1(
                value["validation_status"]
            )
        )
    if "resource_record" in value:
        import aws_sdk_acm.types.resource_record

        out["ResourceRecord"] = (
            aws_sdk_acm.types.resource_record.serialize_aws_json_1_1(
                value["resource_record"]
            )
        )
    if "http_redirect" in value:
        import aws_sdk_acm.types.http_redirect

        out["HttpRedirect"] = aws_sdk_acm.types.http_redirect.serialize_aws_json_1_1(
            value["http_redirect"]
        )
    if "validation_method" in value:
        import aws_sdk_acm.types.validation_method

        out["ValidationMethod"] = (
            aws_sdk_acm.types.validation_method.serialize_aws_json_1_1(
                value["validation_method"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DomainValidation:
    out: DomainValidation = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError("DomainValidation.domain_name required")
    if "ValidationEmails" in data:
        import aws_sdk_acm.types.validation_email_list

        out["validation_emails"] = (
            aws_sdk_acm.types.validation_email_list.deserialize_aws_json_1_1(
                data["ValidationEmails"]
            )
        )
    if "ValidationDomain" in data:
        out["validation_domain"] = data["ValidationDomain"]
    if "ValidationStatus" in data:
        import aws_sdk_acm.types.domain_status

        out["validation_status"] = (
            aws_sdk_acm.types.domain_status.deserialize_aws_json_1_1(
                data["ValidationStatus"]
            )
        )
    if "ResourceRecord" in data:
        import aws_sdk_acm.types.resource_record

        out["resource_record"] = (
            aws_sdk_acm.types.resource_record.deserialize_aws_json_1_1(
                data["ResourceRecord"]
            )
        )
    if "HttpRedirect" in data:
        import aws_sdk_acm.types.http_redirect

        out["http_redirect"] = aws_sdk_acm.types.http_redirect.deserialize_aws_json_1_1(
            data["HttpRedirect"]
        )
    if "ValidationMethod" in data:
        import aws_sdk_acm.types.validation_method

        out["validation_method"] = (
            aws_sdk_acm.types.validation_method.deserialize_aws_json_1_1(
                data["ValidationMethod"]
            )
        )
    return out
