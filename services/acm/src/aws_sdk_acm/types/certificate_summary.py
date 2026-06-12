"""Generated from Smithy shape ``com.amazonaws.acm#CertificateSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_acm.types.arn
    import aws_sdk_acm.types.certificate_export
    import aws_sdk_acm.types.certificate_managed_by
    import aws_sdk_acm.types.certificate_status
    import aws_sdk_acm.types.certificate_type
    import aws_sdk_acm.types.domain_list
    import aws_sdk_acm.types.domain_name_string
    import aws_sdk_acm.types.extended_key_usage_names
    import aws_sdk_acm.types.key_algorithm
    import aws_sdk_acm.types.key_usage_names
    import aws_sdk_acm.types.nullable_boolean
    import aws_sdk_acm.types.renewal_eligibility
    import aws_sdk_acm.types.t_stamp


class CertificateSummary(TypedDict):
    certificate_arn: NotRequired["aws_sdk_acm.types.arn.Arn"]
    """<p>Amazon Resource Name (ARN) of the certificate. This is of the form:</p> <p> <code>arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012</code> </p> <p>For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs)</a>.</p>"""
    domain_name: NotRequired["aws_sdk_acm.types.domain_name_string.DomainNameString"]
    """<p>Fully qualified domain name (FQDN), such as www.example.com or example.com, for the certificate.</p>"""
    subject_alternative_name_summaries: NotRequired[
        "aws_sdk_acm.types.domain_list.DomainList"
    ]
    """<p>One or more domain names (subject alternative names) included in the certificate. This list contains the domain names that are bound to the public key that is contained in the certificate. The subject alternative names include the canonical domain name (CN) of the certificate and additional domain names that can be used to connect to the website. </p> <p>When called by <a href=\"https://docs.aws.amazon.com/acm/latest/APIReference/API_ListCertificates.html\">ListCertificates</a>, this parameter will only return the first 100 subject alternative names included in the certificate. To display the full list of subject alternative names, use <a href=\"https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeCertificate.html\">DescribeCertificate</a>.</p>"""
    has_additional_subject_alternative_names: NotRequired[
        "aws_sdk_acm.types.nullable_boolean.NullableBoolean"
    ]
    """<p>When called by <a href=\"https://docs.aws.amazon.com/acm/latest/APIReference/API_ListCertificates.html\">ListCertificates</a>, indicates whether the full list of subject alternative names has been included in the response. If false, the response includes all of the subject alternative names included in the certificate. If true, the response only includes the first 100 subject alternative names included in the certificate. To display the full list of subject alternative names, use <a href=\"https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeCertificate.html\">DescribeCertificate</a>.</p>"""
    status: NotRequired["aws_sdk_acm.types.certificate_status.CertificateStatus"]
    """<p>The status of the certificate.</p> <p>A certificate enters status PENDING_VALIDATION upon being requested, unless it fails for any of the reasons given in the troubleshooting topic <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/troubleshooting-failed.html\">Certificate request fails</a>. ACM makes repeated attempts to validate a certificate for 72 hours and then times out. If a certificate shows status FAILED or VALIDATION_TIMED_OUT, delete the request, correct the issue with <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/dns-validation.html\">DNS validation</a> or <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/email-validation.html\">Email validation</a>, and try again. If validation succeeds, the certificate enters status ISSUED. </p>"""
    type: NotRequired["aws_sdk_acm.types.certificate_type.CertificateType"]
    """<p>The source of the certificate. For certificates provided by ACM, this value is <code>AMAZON_ISSUED</code>. For certificates that you imported with <a>ImportCertificate</a>, this value is <code>IMPORTED</code>. ACM does not provide <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html\">managed renewal</a> for imported certificates. For more information about the differences between certificates that you import and those that ACM provides, see <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html\">Importing Certificates</a> in the <i>Certificate Manager User Guide</i>. </p>"""
    key_algorithm: NotRequired["aws_sdk_acm.types.key_algorithm.KeyAlgorithm"]
    """<p>The algorithm that was used to generate the public-private key pair.</p>"""
    key_usages: NotRequired["aws_sdk_acm.types.key_usage_names.KeyUsageNames"]
    """<p>A list of Key Usage X.509 v3 extension objects. Each object is a string value that identifies the purpose of the public key contained in the certificate. Possible extension values include DIGITAL_SIGNATURE, KEY_ENCHIPHERMENT, NON_REPUDIATION, and more.</p>"""
    extended_key_usages: NotRequired[
        "aws_sdk_acm.types.extended_key_usage_names.ExtendedKeyUsageNames"
    ]
    """<p>Contains a list of Extended Key Usage X.509 v3 extension objects. Each object specifies a purpose for which the certificate public key can be used and consists of a name and an object identifier (OID). </p>"""
    export_option: NotRequired["aws_sdk_acm.types.certificate_export.CertificateExport"]
    """<p>Indicates if export is enabled for the certificate.</p>"""
    in_use: NotRequired["aws_sdk_acm.types.nullable_boolean.NullableBoolean"]
    """<p>Indicates whether the certificate is currently in use by any Amazon Web Services resources.</p>"""
    exported: NotRequired["aws_sdk_acm.types.nullable_boolean.NullableBoolean"]
    """<p>Indicates whether the certificate has been exported. This value exists only when the certificate type is <code>PRIVATE</code>.</p>"""
    renewal_eligibility: NotRequired[
        "aws_sdk_acm.types.renewal_eligibility.RenewalEligibility"
    ]
    """<p>Specifies whether the certificate is eligible for renewal. At this time, only exported private certificates can be renewed with the <a>RenewCertificate</a> command.</p>"""
    not_before: NotRequired["aws_sdk_acm.types.t_stamp.TStamp"]
    """<p>The time before which the certificate is not valid.</p>"""
    not_after: NotRequired["aws_sdk_acm.types.t_stamp.TStamp"]
    """<p>The time after which the certificate is not valid.</p>"""
    created_at: NotRequired["aws_sdk_acm.types.t_stamp.TStamp"]
    """<p>The time at which the certificate was requested.</p>"""
    issued_at: NotRequired["aws_sdk_acm.types.t_stamp.TStamp"]
    """<p>The time at which the certificate was issued. This value exists only when the certificate type is <code>AMAZON_ISSUED</code>. </p>"""
    imported_at: NotRequired["aws_sdk_acm.types.t_stamp.TStamp"]
    """<p>The date and time when the certificate was imported. This value exists only when the certificate type is <code>IMPORTED</code>. </p>"""
    revoked_at: NotRequired["aws_sdk_acm.types.t_stamp.TStamp"]
    """<p>The time at which the certificate was revoked. This value exists only when the certificate status is <code>REVOKED</code>. </p>"""
    managed_by: NotRequired[
        "aws_sdk_acm.types.certificate_managed_by.CertificateManagedBy"
    ]
    """<p>Identifies the Amazon Web Services service that manages the certificate issued by ACM.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateSummary) -> dict:
    out: dict = {}
    if "certificate_arn" in value:
        out["CertificateArn"] = value["certificate_arn"]
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "subject_alternative_name_summaries" in value:
        import aws_sdk_acm.types.domain_list

        out["SubjectAlternativeNameSummaries"] = (
            aws_sdk_acm.types.domain_list.serialize_aws_json_1_1(
                value["subject_alternative_name_summaries"]
            )
        )
    if "has_additional_subject_alternative_names" in value:
        out["HasAdditionalSubjectAlternativeNames"] = value[
            "has_additional_subject_alternative_names"
        ]
    if "status" in value:
        import aws_sdk_acm.types.certificate_status

        out["Status"] = aws_sdk_acm.types.certificate_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "type" in value:
        import aws_sdk_acm.types.certificate_type

        out["Type"] = aws_sdk_acm.types.certificate_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "key_algorithm" in value:
        import aws_sdk_acm.types.key_algorithm

        out["KeyAlgorithm"] = aws_sdk_acm.types.key_algorithm.serialize_aws_json_1_1(
            value["key_algorithm"]
        )
    if "key_usages" in value:
        import aws_sdk_acm.types.key_usage_names

        out["KeyUsages"] = aws_sdk_acm.types.key_usage_names.serialize_aws_json_1_1(
            value["key_usages"]
        )
    if "extended_key_usages" in value:
        import aws_sdk_acm.types.extended_key_usage_names

        out["ExtendedKeyUsages"] = (
            aws_sdk_acm.types.extended_key_usage_names.serialize_aws_json_1_1(
                value["extended_key_usages"]
            )
        )
    if "export_option" in value:
        import aws_sdk_acm.types.certificate_export

        out["ExportOption"] = (
            aws_sdk_acm.types.certificate_export.serialize_aws_json_1_1(
                value["export_option"]
            )
        )
    if "in_use" in value:
        out["InUse"] = value["in_use"]
    if "exported" in value:
        out["Exported"] = value["exported"]
    if "renewal_eligibility" in value:
        import aws_sdk_acm.types.renewal_eligibility

        out["RenewalEligibility"] = (
            aws_sdk_acm.types.renewal_eligibility.serialize_aws_json_1_1(
                value["renewal_eligibility"]
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
    if "revoked_at" in value:
        import aws_sdk_acm.types.t_stamp

        out["RevokedAt"] = aws_sdk_acm.types.t_stamp.serialize_aws_json_1_1(
            value["revoked_at"]
        )
    if "managed_by" in value:
        import aws_sdk_acm.types.certificate_managed_by

        out["ManagedBy"] = (
            aws_sdk_acm.types.certificate_managed_by.serialize_aws_json_1_1(
                value["managed_by"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CertificateSummary:
    out: CertificateSummary = {}  # type: ignore[typeddict-item]
    if "CertificateArn" in data:
        out["certificate_arn"] = data["CertificateArn"]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    if "SubjectAlternativeNameSummaries" in data:
        import aws_sdk_acm.types.domain_list

        out["subject_alternative_name_summaries"] = (
            aws_sdk_acm.types.domain_list.deserialize_aws_json_1_1(
                data["SubjectAlternativeNameSummaries"]
            )
        )
    if "HasAdditionalSubjectAlternativeNames" in data:
        out["has_additional_subject_alternative_names"] = data[
            "HasAdditionalSubjectAlternativeNames"
        ]
    if "Status" in data:
        import aws_sdk_acm.types.certificate_status

        out["status"] = aws_sdk_acm.types.certificate_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "Type" in data:
        import aws_sdk_acm.types.certificate_type

        out["type"] = aws_sdk_acm.types.certificate_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "KeyAlgorithm" in data:
        import aws_sdk_acm.types.key_algorithm

        out["key_algorithm"] = aws_sdk_acm.types.key_algorithm.deserialize_aws_json_1_1(
            data["KeyAlgorithm"]
        )
    if "KeyUsages" in data:
        import aws_sdk_acm.types.key_usage_names

        out["key_usages"] = aws_sdk_acm.types.key_usage_names.deserialize_aws_json_1_1(
            data["KeyUsages"]
        )
    if "ExtendedKeyUsages" in data:
        import aws_sdk_acm.types.extended_key_usage_names

        out["extended_key_usages"] = (
            aws_sdk_acm.types.extended_key_usage_names.deserialize_aws_json_1_1(
                data["ExtendedKeyUsages"]
            )
        )
    if "ExportOption" in data:
        import aws_sdk_acm.types.certificate_export

        out["export_option"] = (
            aws_sdk_acm.types.certificate_export.deserialize_aws_json_1_1(
                data["ExportOption"]
            )
        )
    if "InUse" in data:
        out["in_use"] = data["InUse"]
    if "Exported" in data:
        out["exported"] = data["Exported"]
    if "RenewalEligibility" in data:
        import aws_sdk_acm.types.renewal_eligibility

        out["renewal_eligibility"] = (
            aws_sdk_acm.types.renewal_eligibility.deserialize_aws_json_1_1(
                data["RenewalEligibility"]
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
    if "RevokedAt" in data:
        import aws_sdk_acm.types.t_stamp

        out["revoked_at"] = aws_sdk_acm.types.t_stamp.deserialize_aws_json_1_1(
            data["RevokedAt"]
        )
    if "ManagedBy" in data:
        import aws_sdk_acm.types.certificate_managed_by

        out["managed_by"] = (
            aws_sdk_acm.types.certificate_managed_by.deserialize_aws_json_1_1(
                data["ManagedBy"]
            )
        )
    return out
