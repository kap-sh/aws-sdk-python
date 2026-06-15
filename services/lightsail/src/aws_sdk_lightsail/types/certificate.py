"""Generated from Smithy shape ``com.amazonaws.lightsail#Certificate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.certificate_name
    import aws_sdk_lightsail.types.certificate_status
    import aws_sdk_lightsail.types.domain_name
    import aws_sdk_lightsail.types.domain_validation_record_list
    import aws_sdk_lightsail.types.eligible_to_renew
    import aws_sdk_lightsail.types.in_use_resource_count
    import aws_sdk_lightsail.types.iso_date
    import aws_sdk_lightsail.types.issuer_ca
    import aws_sdk_lightsail.types.key_algorithm
    import aws_sdk_lightsail.types.non_empty_string
    import aws_sdk_lightsail.types.renewal_summary
    import aws_sdk_lightsail.types.request_failure_reason
    import aws_sdk_lightsail.types.revocation_reason
    import aws_sdk_lightsail.types.serial_number
    import aws_sdk_lightsail.types.string
    import aws_sdk_lightsail.types.subject_alternative_name_list
    import aws_sdk_lightsail.types.tag_list


class Certificate(TypedDict):
    arn: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the certificate.</p>"""
    name: NotRequired["aws_sdk_lightsail.types.certificate_name.CertificateName"]
    """<p>The name of the certificate (<code>my-certificate</code>).</p>"""
    domain_name: NotRequired["aws_sdk_lightsail.types.domain_name.DomainName"]
    """<p>The domain name of the certificate.</p>"""
    status: NotRequired["aws_sdk_lightsail.types.certificate_status.CertificateStatus"]
    """<p>The validation status of the certificate.</p>"""
    serial_number: NotRequired["aws_sdk_lightsail.types.serial_number.SerialNumber"]
    """<p>The serial number of the certificate.</p>"""
    subject_alternative_names: NotRequired[
        "aws_sdk_lightsail.types.subject_alternative_name_list.SubjectAlternativeNameList"
    ]
    """<p>An array of strings that specify the alternate domains (<code>example2.com</code>) and subdomains (<code>blog.example.com</code>) of the certificate.</p>"""
    domain_validation_records: NotRequired[
        "aws_sdk_lightsail.types.domain_validation_record_list.DomainValidationRecordList"
    ]
    """<p>An array of objects that describe the domain validation records of the certificate.</p>"""
    request_failure_reason: NotRequired[
        "aws_sdk_lightsail.types.request_failure_reason.RequestFailureReason"
    ]
    r"""<p>The validation failure reason, if any, of the certificate.</p> <p>The following failure reasons are possible:</p> <ul> <li> <p> <b> <code>NO_AVAILABLE_CONTACTS</code> </b> - This failure applies to email validation, which is not available for Lightsail certificates.</p> </li> <li> <p> <b> <code>ADDITIONAL_VERIFICATION_REQUIRED</code> </b> - Lightsail requires additional information to process this certificate request. This can happen as a fraud-protection measure, such as when the domain ranks within the Alexa top 1000 websites. To provide the required information, use the <a href=\"https://console.aws.amazon.com/support/home\">Amazon Web Services Support Center</a> to contact Amazon Web Services Support.</p> <note> <p>You cannot request a certificate for Amazon-owned domain names such as those ending in amazonaws.com, cloudfront.net, or elasticbeanstalk.com.</p> </note> </li> <li> <p> <b> <code>DOMAIN_NOT_ALLOWED</code> </b> - One or more of the domain names in the certificate request was reported as an unsafe domain by <a href=\"https://www.virustotal.com/gui/home/url\">VirusTotal</a>. To correct the problem, search for your domain name on the <a href=\"https://www.virustotal.com/gui/home/url\">VirusTotal</a> website. If your domain is reported as suspicious, see <a href=\"https://developers.google.com/web/fundamentals/security/hacked\">Google Help for Hacked Websites</a> to learn what you can do.</p> <p>If you believe that the result is a false positive, notify the organization that is reporting the domain. VirusTotal is an aggregate of several antivirus and URL scanners and cannot remove your domain from a block list itself. After you correct the problem and the VirusTotal registry has been updated, request a new certificate.</p> <p>If you see this error and your domain is not included in the VirusTotal list, visit the <a href=\"https://console.aws.amazon.com/support/home\">Amazon Web Services Support Center</a> and create a case.</p> </li> <li> <p> <b> <code>INVALID_PUBLIC_DOMAIN</code> </b> - One or more of the domain names in the certificate request is not valid. Typically, this is because a domain name in the request is not a valid top-level domain. Try to request a certificate again, correcting any spelling errors or typos that were in the failed request, and ensure that all domain names in the request are for valid top-level domains. For example, you cannot request a certificate for <code>example.invalidpublicdomain</code> because <code>invalidpublicdomain</code> is not a valid top-level domain.</p> </li> <li> <p> <b> <code>OTHER</code> </b> - Typically, this failure occurs when there is a typographical error in one or more of the domain names in the certificate request. Try to request a certificate again, correcting any spelling errors or typos that were in the failed request. </p> </li> </ul>"""
    in_use_resource_count: (
        "aws_sdk_lightsail.types.in_use_resource_count.InUseResourceCount"
    )
    """<p>The number of Lightsail resources that the certificate is attached to.</p>"""
    key_algorithm: NotRequired["aws_sdk_lightsail.types.key_algorithm.KeyAlgorithm"]
    """<p>The algorithm used to generate the key pair (the public and private key) of the certificate.</p>"""
    created_at: NotRequired["aws_sdk_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the certificate was created.</p>"""
    issued_at: NotRequired["aws_sdk_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the certificate was issued.</p>"""
    issuer_ca: NotRequired["aws_sdk_lightsail.types.issuer_ca.IssuerCA"]
    """<p>The certificate authority that issued the certificate.</p>"""
    not_before: NotRequired["aws_sdk_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the certificate is first valid.</p>"""
    not_after: NotRequired["aws_sdk_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the certificate expires.</p>"""
    eligible_to_renew: NotRequired[
        "aws_sdk_lightsail.types.eligible_to_renew.EligibleToRenew"
    ]
    """<p>The renewal eligibility of the certificate.</p>"""
    renewal_summary: NotRequired[
        "aws_sdk_lightsail.types.renewal_summary.RenewalSummary"
    ]
    """<p>An object that describes the status of the certificate renewal managed by Lightsail.</p>"""
    revoked_at: NotRequired["aws_sdk_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the certificate was revoked. This value is present only when the certificate status is <code>REVOKED</code>.</p>"""
    revocation_reason: NotRequired[
        "aws_sdk_lightsail.types.revocation_reason.RevocationReason"
    ]
    """<p>The reason the certificate was revoked. This value is present only when the certificate status is <code>REVOKED</code>.</p>"""
    tags: NotRequired["aws_sdk_lightsail.types.tag_list.TagList"]
    r"""<p>The tag keys and optional values for the resource. For more information about tags in Lightsail, see the <a href=\"https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags\">Amazon Lightsail Developer Guide</a>.</p>"""
    support_code: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The support code. Include this code in your email to support when you have questions about your Lightsail certificate. This code enables our support team to look up your Lightsail information more easily.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Certificate) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "domain_name" in value:
        out["domainName"] = value["domain_name"]
    if "status" in value:
        import aws_sdk_lightsail.types.certificate_status

        out["status"] = (
            aws_sdk_lightsail.types.certificate_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "serial_number" in value:
        out["serialNumber"] = value["serial_number"]
    if "subject_alternative_names" in value:
        import aws_sdk_lightsail.types.subject_alternative_name_list

        out["subjectAlternativeNames"] = (
            aws_sdk_lightsail.types.subject_alternative_name_list.serialize_aws_json_1_1(
                value["subject_alternative_names"]
            )
        )
    if "domain_validation_records" in value:
        import aws_sdk_lightsail.types.domain_validation_record_list

        out["domainValidationRecords"] = (
            aws_sdk_lightsail.types.domain_validation_record_list.serialize_aws_json_1_1(
                value["domain_validation_records"]
            )
        )
    if "request_failure_reason" in value:
        out["requestFailureReason"] = value["request_failure_reason"]
    out["inUseResourceCount"] = value.get("in_use_resource_count", 0)
    if "key_algorithm" in value:
        out["keyAlgorithm"] = value["key_algorithm"]
    if "created_at" in value:
        import aws_sdk_lightsail.types.iso_date

        out["createdAt"] = aws_sdk_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "issued_at" in value:
        import aws_sdk_lightsail.types.iso_date

        out["issuedAt"] = aws_sdk_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["issued_at"]
        )
    if "issuer_ca" in value:
        out["issuerCA"] = value["issuer_ca"]
    if "not_before" in value:
        import aws_sdk_lightsail.types.iso_date

        out["notBefore"] = aws_sdk_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["not_before"]
        )
    if "not_after" in value:
        import aws_sdk_lightsail.types.iso_date

        out["notAfter"] = aws_sdk_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["not_after"]
        )
    if "eligible_to_renew" in value:
        out["eligibleToRenew"] = value["eligible_to_renew"]
    if "renewal_summary" in value:
        import aws_sdk_lightsail.types.renewal_summary

        out["renewalSummary"] = (
            aws_sdk_lightsail.types.renewal_summary.serialize_aws_json_1_1(
                value["renewal_summary"]
            )
        )
    if "revoked_at" in value:
        import aws_sdk_lightsail.types.iso_date

        out["revokedAt"] = aws_sdk_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["revoked_at"]
        )
    if "revocation_reason" in value:
        out["revocationReason"] = value["revocation_reason"]
    if "tags" in value:
        import aws_sdk_lightsail.types.tag_list

        out["tags"] = aws_sdk_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "support_code" in value:
        out["supportCode"] = value["support_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Certificate:
    out: Certificate = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    if "status" in data:
        import aws_sdk_lightsail.types.certificate_status

        out["status"] = (
            aws_sdk_lightsail.types.certificate_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "serialNumber" in data:
        out["serial_number"] = data["serialNumber"]
    if "subjectAlternativeNames" in data:
        import aws_sdk_lightsail.types.subject_alternative_name_list

        out["subject_alternative_names"] = (
            aws_sdk_lightsail.types.subject_alternative_name_list.deserialize_aws_json_1_1(
                data["subjectAlternativeNames"]
            )
        )
    if "domainValidationRecords" in data:
        import aws_sdk_lightsail.types.domain_validation_record_list

        out["domain_validation_records"] = (
            aws_sdk_lightsail.types.domain_validation_record_list.deserialize_aws_json_1_1(
                data["domainValidationRecords"]
            )
        )
    if "requestFailureReason" in data:
        out["request_failure_reason"] = data["requestFailureReason"]
    if "inUseResourceCount" in data:
        out["in_use_resource_count"] = data["inUseResourceCount"]
    else:
        out["in_use_resource_count"] = 0
    if "keyAlgorithm" in data:
        out["key_algorithm"] = data["keyAlgorithm"]
    if "createdAt" in data:
        import aws_sdk_lightsail.types.iso_date

        out["created_at"] = aws_sdk_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if "issuedAt" in data:
        import aws_sdk_lightsail.types.iso_date

        out["issued_at"] = aws_sdk_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["issuedAt"]
        )
    if "issuerCA" in data:
        out["issuer_ca"] = data["issuerCA"]
    if "notBefore" in data:
        import aws_sdk_lightsail.types.iso_date

        out["not_before"] = aws_sdk_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["notBefore"]
        )
    if "notAfter" in data:
        import aws_sdk_lightsail.types.iso_date

        out["not_after"] = aws_sdk_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["notAfter"]
        )
    if "eligibleToRenew" in data:
        out["eligible_to_renew"] = data["eligibleToRenew"]
    if "renewalSummary" in data:
        import aws_sdk_lightsail.types.renewal_summary

        out["renewal_summary"] = (
            aws_sdk_lightsail.types.renewal_summary.deserialize_aws_json_1_1(
                data["renewalSummary"]
            )
        )
    if "revokedAt" in data:
        import aws_sdk_lightsail.types.iso_date

        out["revoked_at"] = aws_sdk_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["revokedAt"]
        )
    if "revocationReason" in data:
        out["revocation_reason"] = data["revocationReason"]
    if "tags" in data:
        import aws_sdk_lightsail.types.tag_list

        out["tags"] = aws_sdk_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if "supportCode" in data:
        out["support_code"] = data["supportCode"]
    return out
