"""Generated from Smithy shape ``com.amazonaws.acm#CertificateDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_acm.types.arn
    import aws_sdk_acm.types.certificate_managed_by
    import aws_sdk_acm.types.certificate_options
    import aws_sdk_acm.types.certificate_status
    import aws_sdk_acm.types.certificate_type
    import aws_sdk_acm.types.domain_list
    import aws_sdk_acm.types.domain_name_string
    import aws_sdk_acm.types.domain_validation_list
    import aws_sdk_acm.types.extended_key_usage_list
    import aws_sdk_acm.types.failure_reason
    import aws_sdk_acm.types.in_use_list
    import aws_sdk_acm.types.key_algorithm
    import aws_sdk_acm.types.key_usage_list
    import aws_sdk_acm.types.renewal_eligibility
    import aws_sdk_acm.types.renewal_summary
    import aws_sdk_acm.types.revocation_reason
    import aws_sdk_acm.types.string
    import aws_sdk_acm.types.t_stamp


class CertificateDetail(TypedDict):
    certificate_arn: NotRequired["aws_sdk_acm.types.arn.Arn"]
    r"""<p>The Amazon Resource Name (ARN) of the certificate. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    domain_name: NotRequired["aws_sdk_acm.types.domain_name_string.DomainNameString"]
    """<p>The fully qualified domain name for the certificate, such as www.example.com or example.com.</p>"""
    subject_alternative_names: NotRequired["aws_sdk_acm.types.domain_list.DomainList"]
    """<p>One or more domain names (subject alternative names) included in the certificate. This list contains the domain names that are bound to the public key that is contained in the certificate. The subject alternative names include the canonical domain name (CN) of the certificate and additional domain names that can be used to connect to the website. </p>"""
    managed_by: NotRequired[
        "aws_sdk_acm.types.certificate_managed_by.CertificateManagedBy"
    ]
    """<p>Identifies the Amazon Web Services service that manages the certificate issued by ACM.</p>"""
    domain_validation_options: NotRequired[
        "aws_sdk_acm.types.domain_validation_list.DomainValidationList"
    ]
    """<p>Contains information about the initial validation of each domain name that occurs as a result of the <a>RequestCertificate</a> request. This field exists only when the certificate type is <code>AMAZON_ISSUED</code>. </p>"""
    serial: NotRequired["aws_sdk_acm.types.string.String"]
    """<p>The serial number of the certificate.</p>"""
    subject: NotRequired["aws_sdk_acm.types.string.String"]
    """<p>The name of the entity that is associated with the public key contained in the certificate.</p>"""
    issuer: NotRequired["aws_sdk_acm.types.string.String"]
    """<p>The name of the certificate authority that issued and signed the certificate.</p>"""
    created_at: NotRequired["aws_sdk_acm.types.t_stamp.TStamp"]
    """<p>The time at which the certificate was requested.</p>"""
    issued_at: NotRequired["aws_sdk_acm.types.t_stamp.TStamp"]
    """<p>The time at which the certificate was issued. This value exists only when the certificate type is <code>AMAZON_ISSUED</code>. </p>"""
    imported_at: NotRequired["aws_sdk_acm.types.t_stamp.TStamp"]
    """<p>The date and time when the certificate was imported. This value exists only when the certificate type is <code>IMPORTED</code>. </p>"""
    status: NotRequired["aws_sdk_acm.types.certificate_status.CertificateStatus"]
    r"""<p>The status of the certificate.</p> <p>A certificate enters status PENDING_VALIDATION upon being requested, unless it fails for any of the reasons given in the troubleshooting topic <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/troubleshooting-failed.html\">Certificate request fails</a>. ACM makes repeated attempts to validate a certificate for 72 hours and then times out. If a certificate shows status FAILED or VALIDATION_TIMED_OUT, delete the request, correct the issue with <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/dns-validation.html\">DNS validation</a> or <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/email-validation.html\">Email validation</a>, and try again. If validation succeeds, the certificate enters status ISSUED. </p>"""
    revoked_at: NotRequired["aws_sdk_acm.types.t_stamp.TStamp"]
    """<p>The time at which the certificate was revoked. This value exists only when the certificate status is <code>REVOKED</code>. </p>"""
    revocation_reason: NotRequired[
        "aws_sdk_acm.types.revocation_reason.RevocationReason"
    ]
    """<p>The reason the certificate was revoked. This value exists only when the certificate status is <code>REVOKED</code>. </p>"""
    not_before: NotRequired["aws_sdk_acm.types.t_stamp.TStamp"]
    """<p>The time before which the certificate is not valid.</p>"""
    not_after: NotRequired["aws_sdk_acm.types.t_stamp.TStamp"]
    """<p>The time after which the certificate is not valid.</p>"""
    key_algorithm: NotRequired["aws_sdk_acm.types.key_algorithm.KeyAlgorithm"]
    """<p>The algorithm that was used to generate the public-private key pair.</p>"""
    signature_algorithm: NotRequired["aws_sdk_acm.types.string.String"]
    """<p>The algorithm that was used to sign the certificate.</p>"""
    in_use_by: NotRequired["aws_sdk_acm.types.in_use_list.InUseList"]
    """<p>A list of ARNs for the Amazon Web Services resources that are using the certificate. A certificate can be used by multiple Amazon Web Services resources. </p>"""
    failure_reason: NotRequired["aws_sdk_acm.types.failure_reason.FailureReason"]
    r"""<p>The reason the certificate request failed. This value exists only when the certificate status is <code>FAILED</code>. For more information, see <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/troubleshooting.html#troubleshooting-failed\">Certificate Request Failed</a> in the <i>Certificate Manager User Guide</i>. </p>"""
    type: NotRequired["aws_sdk_acm.types.certificate_type.CertificateType"]
    r"""<p>The source of the certificate. For certificates provided by ACM, this value is <code>AMAZON_ISSUED</code>. For certificates that you imported with <a>ImportCertificate</a>, this value is <code>IMPORTED</code>. ACM does not provide <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html\">managed renewal</a> for imported certificates. For more information about the differences between certificates that you import and those that ACM provides, see <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html\">Importing Certificates</a> in the <i>Certificate Manager User Guide</i>. </p>"""
    renewal_summary: NotRequired["aws_sdk_acm.types.renewal_summary.RenewalSummary"]
    r"""<p>Contains information about the status of ACM's <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html\">managed renewal</a> for the certificate. This field exists only when the certificate type is <code>AMAZON_ISSUED</code>.</p>"""
    key_usages: NotRequired["aws_sdk_acm.types.key_usage_list.KeyUsageList"]
    """<p>A list of Key Usage X.509 v3 extension objects. Each object is a string value that identifies the purpose of the public key contained in the certificate. Possible extension values include DIGITAL_SIGNATURE, KEY_ENCHIPHERMENT, NON_REPUDIATION, and more.</p>"""
    extended_key_usages: NotRequired[
        "aws_sdk_acm.types.extended_key_usage_list.ExtendedKeyUsageList"
    ]
    """<p>Contains a list of Extended Key Usage X.509 v3 extension objects. Each object specifies a purpose for which the certificate public key can be used and consists of a name and an object identifier (OID). </p>"""
    certificate_authority_arn: NotRequired["aws_sdk_acm.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the private certificate authority (CA) that issued the certificate. This has the following format: </p> <p> <code>arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012</code> </p>"""
    renewal_eligibility: NotRequired[
        "aws_sdk_acm.types.renewal_eligibility.RenewalEligibility"
    ]
    """<p>Specifies whether the certificate is eligible for renewal. At this time, only exported private certificates can be renewed with the <a>RenewCertificate</a> command.</p>"""
    options: NotRequired["aws_sdk_acm.types.certificate_options.CertificateOptions"]
    """<p>Value that specifies whether to add the certificate to a transparency log. Certificate transparency makes it possible to detect SSL certificates that have been mistakenly or maliciously issued. A browser might respond to certificate that has not been logged by showing an error message. The logs are cryptographically secure. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateDetail) -> dict:
    out: dict = {}
    if "certificate_arn" in value:
        out["CertificateArn"] = value["certificate_arn"]
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "subject_alternative_names" in value:
        import aws_sdk_acm.types.domain_list

        out["SubjectAlternativeNames"] = (
            aws_sdk_acm.types.domain_list.serialize_aws_json_1_1(
                value["subject_alternative_names"]
            )
        )
    if "managed_by" in value:
        import aws_sdk_acm.types.certificate_managed_by

        out["ManagedBy"] = (
            aws_sdk_acm.types.certificate_managed_by.serialize_aws_json_1_1(
                value["managed_by"]
            )
        )
    if "domain_validation_options" in value:
        import aws_sdk_acm.types.domain_validation_list

        out["DomainValidationOptions"] = (
            aws_sdk_acm.types.domain_validation_list.serialize_aws_json_1_1(
                value["domain_validation_options"]
            )
        )
    if "serial" in value:
        out["Serial"] = value["serial"]
    if "subject" in value:
        out["Subject"] = value["subject"]
    if "issuer" in value:
        out["Issuer"] = value["issuer"]
    if "created_at" in value:
        import aws_sdk_acm.types.t_stamp

        out["CreatedAt"] = aws_sdk_acm.types.t_stamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "issued_at" in value:
        import aws_sdk_acm.types.t_stamp

        out["IssuedAt"] = aws_sdk_acm.types.t_stamp.serialize_aws_json_1_1(
            value["issued_at"]
        )
    if "imported_at" in value:
        import aws_sdk_acm.types.t_stamp

        out["ImportedAt"] = aws_sdk_acm.types.t_stamp.serialize_aws_json_1_1(
            value["imported_at"]
        )
    if "status" in value:
        import aws_sdk_acm.types.certificate_status

        out["Status"] = aws_sdk_acm.types.certificate_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "revoked_at" in value:
        import aws_sdk_acm.types.t_stamp

        out["RevokedAt"] = aws_sdk_acm.types.t_stamp.serialize_aws_json_1_1(
            value["revoked_at"]
        )
    if "revocation_reason" in value:
        import aws_sdk_acm.types.revocation_reason

        out["RevocationReason"] = (
            aws_sdk_acm.types.revocation_reason.serialize_aws_json_1_1(
                value["revocation_reason"]
            )
        )
    if "not_before" in value:
        import aws_sdk_acm.types.t_stamp

        out["NotBefore"] = aws_sdk_acm.types.t_stamp.serialize_aws_json_1_1(
            value["not_before"]
        )
    if "not_after" in value:
        import aws_sdk_acm.types.t_stamp

        out["NotAfter"] = aws_sdk_acm.types.t_stamp.serialize_aws_json_1_1(
            value["not_after"]
        )
    if "key_algorithm" in value:
        import aws_sdk_acm.types.key_algorithm

        out["KeyAlgorithm"] = aws_sdk_acm.types.key_algorithm.serialize_aws_json_1_1(
            value["key_algorithm"]
        )
    if "signature_algorithm" in value:
        out["SignatureAlgorithm"] = value["signature_algorithm"]
    if "in_use_by" in value:
        import aws_sdk_acm.types.in_use_list

        out["InUseBy"] = aws_sdk_acm.types.in_use_list.serialize_aws_json_1_1(
            value["in_use_by"]
        )
    if "failure_reason" in value:
        import aws_sdk_acm.types.failure_reason

        out["FailureReason"] = aws_sdk_acm.types.failure_reason.serialize_aws_json_1_1(
            value["failure_reason"]
        )
    if "type" in value:
        import aws_sdk_acm.types.certificate_type

        out["Type"] = aws_sdk_acm.types.certificate_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "renewal_summary" in value:
        import aws_sdk_acm.types.renewal_summary

        out["RenewalSummary"] = (
            aws_sdk_acm.types.renewal_summary.serialize_aws_json_1_1(
                value["renewal_summary"]
            )
        )
    if "key_usages" in value:
        import aws_sdk_acm.types.key_usage_list

        out["KeyUsages"] = aws_sdk_acm.types.key_usage_list.serialize_aws_json_1_1(
            value["key_usages"]
        )
    if "extended_key_usages" in value:
        import aws_sdk_acm.types.extended_key_usage_list

        out["ExtendedKeyUsages"] = (
            aws_sdk_acm.types.extended_key_usage_list.serialize_aws_json_1_1(
                value["extended_key_usages"]
            )
        )
    if "certificate_authority_arn" in value:
        out["CertificateAuthorityArn"] = value["certificate_authority_arn"]
    if "renewal_eligibility" in value:
        import aws_sdk_acm.types.renewal_eligibility

        out["RenewalEligibility"] = (
            aws_sdk_acm.types.renewal_eligibility.serialize_aws_json_1_1(
                value["renewal_eligibility"]
            )
        )
    if "options" in value:
        import aws_sdk_acm.types.certificate_options

        out["Options"] = aws_sdk_acm.types.certificate_options.serialize_aws_json_1_1(
            value["options"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CertificateDetail:
    out: CertificateDetail = {}  # type: ignore[typeddict-item]
    if "CertificateArn" in data:
        out["certificate_arn"] = data["CertificateArn"]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    if "SubjectAlternativeNames" in data:
        import aws_sdk_acm.types.domain_list

        out["subject_alternative_names"] = (
            aws_sdk_acm.types.domain_list.deserialize_aws_json_1_1(
                data["SubjectAlternativeNames"]
            )
        )
    if "ManagedBy" in data:
        import aws_sdk_acm.types.certificate_managed_by

        out["managed_by"] = (
            aws_sdk_acm.types.certificate_managed_by.deserialize_aws_json_1_1(
                data["ManagedBy"]
            )
        )
    if "DomainValidationOptions" in data:
        import aws_sdk_acm.types.domain_validation_list

        out["domain_validation_options"] = (
            aws_sdk_acm.types.domain_validation_list.deserialize_aws_json_1_1(
                data["DomainValidationOptions"]
            )
        )
    if "Serial" in data:
        out["serial"] = data["Serial"]
    if "Subject" in data:
        out["subject"] = data["Subject"]
    if "Issuer" in data:
        out["issuer"] = data["Issuer"]
    if "CreatedAt" in data:
        import aws_sdk_acm.types.t_stamp

        out["created_at"] = aws_sdk_acm.types.t_stamp.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if "IssuedAt" in data:
        import aws_sdk_acm.types.t_stamp

        out["issued_at"] = aws_sdk_acm.types.t_stamp.deserialize_aws_json_1_1(
            data["IssuedAt"]
        )
    if "ImportedAt" in data:
        import aws_sdk_acm.types.t_stamp

        out["imported_at"] = aws_sdk_acm.types.t_stamp.deserialize_aws_json_1_1(
            data["ImportedAt"]
        )
    if "Status" in data:
        import aws_sdk_acm.types.certificate_status

        out["status"] = aws_sdk_acm.types.certificate_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "RevokedAt" in data:
        import aws_sdk_acm.types.t_stamp

        out["revoked_at"] = aws_sdk_acm.types.t_stamp.deserialize_aws_json_1_1(
            data["RevokedAt"]
        )
    if "RevocationReason" in data:
        import aws_sdk_acm.types.revocation_reason

        out["revocation_reason"] = (
            aws_sdk_acm.types.revocation_reason.deserialize_aws_json_1_1(
                data["RevocationReason"]
            )
        )
    if "NotBefore" in data:
        import aws_sdk_acm.types.t_stamp

        out["not_before"] = aws_sdk_acm.types.t_stamp.deserialize_aws_json_1_1(
            data["NotBefore"]
        )
    if "NotAfter" in data:
        import aws_sdk_acm.types.t_stamp

        out["not_after"] = aws_sdk_acm.types.t_stamp.deserialize_aws_json_1_1(
            data["NotAfter"]
        )
    if "KeyAlgorithm" in data:
        import aws_sdk_acm.types.key_algorithm

        out["key_algorithm"] = aws_sdk_acm.types.key_algorithm.deserialize_aws_json_1_1(
            data["KeyAlgorithm"]
        )
    if "SignatureAlgorithm" in data:
        out["signature_algorithm"] = data["SignatureAlgorithm"]
    if "InUseBy" in data:
        import aws_sdk_acm.types.in_use_list

        out["in_use_by"] = aws_sdk_acm.types.in_use_list.deserialize_aws_json_1_1(
            data["InUseBy"]
        )
    if "FailureReason" in data:
        import aws_sdk_acm.types.failure_reason

        out["failure_reason"] = (
            aws_sdk_acm.types.failure_reason.deserialize_aws_json_1_1(
                data["FailureReason"]
            )
        )
    if "Type" in data:
        import aws_sdk_acm.types.certificate_type

        out["type"] = aws_sdk_acm.types.certificate_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "RenewalSummary" in data:
        import aws_sdk_acm.types.renewal_summary

        out["renewal_summary"] = (
            aws_sdk_acm.types.renewal_summary.deserialize_aws_json_1_1(
                data["RenewalSummary"]
            )
        )
    if "KeyUsages" in data:
        import aws_sdk_acm.types.key_usage_list

        out["key_usages"] = aws_sdk_acm.types.key_usage_list.deserialize_aws_json_1_1(
            data["KeyUsages"]
        )
    if "ExtendedKeyUsages" in data:
        import aws_sdk_acm.types.extended_key_usage_list

        out["extended_key_usages"] = (
            aws_sdk_acm.types.extended_key_usage_list.deserialize_aws_json_1_1(
                data["ExtendedKeyUsages"]
            )
        )
    if "CertificateAuthorityArn" in data:
        out["certificate_authority_arn"] = data["CertificateAuthorityArn"]
    if "RenewalEligibility" in data:
        import aws_sdk_acm.types.renewal_eligibility

        out["renewal_eligibility"] = (
            aws_sdk_acm.types.renewal_eligibility.deserialize_aws_json_1_1(
                data["RenewalEligibility"]
            )
        )
    if "Options" in data:
        import aws_sdk_acm.types.certificate_options

        out["options"] = aws_sdk_acm.types.certificate_options.deserialize_aws_json_1_1(
            data["Options"]
        )
    return out
