"""Generated from Smithy shape ``com.amazonaws.acmpca#CreateCertificateAuthorityAuditReportRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_acm_pca.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_acm_pca.types.arn
    import aws_sdk_acm_pca.types.audit_report_response_format
    import aws_sdk_acm_pca.types.s3_bucket_name


class CreateCertificateAuthorityAuditReportRequest(TypedDict):
    certificate_authority_arn: "aws_sdk_acm_pca.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the CA to be audited. This is of the form:</p> <p> <code>arn:aws:acm-pca:<i>region</i>:<i>account</i>:certificate-authority/<i>12345678-1234-1234-1234-123456789012</i> </code>.</p>"""
    s3_bucket_name: "aws_sdk_acm_pca.types.s3_bucket_name.S3BucketName"
    """<p>The name of the S3 bucket that will contain the audit report.</p>"""
    audit_report_response_format: (
        "aws_sdk_acm_pca.types.audit_report_response_format.AuditReportResponseFormat"
    )
    """<p>The format in which to create the report. This can be either <b>JSON</b> or <b>CSV</b>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCertificateAuthorityAuditReportRequest) -> dict:
    out: dict = {}
    out["CertificateAuthorityArn"] = value["certificate_authority_arn"]
    out["S3BucketName"] = value["s3_bucket_name"]
    import aws_sdk_acm_pca.types.audit_report_response_format

    out["AuditReportResponseFormat"] = (
        aws_sdk_acm_pca.types.audit_report_response_format.serialize_aws_json_1_1(
            value["audit_report_response_format"]
        )
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> CreateCertificateAuthorityAuditReportRequest:
    out: CreateCertificateAuthorityAuditReportRequest = {}  # type: ignore[typeddict-item]
    if "CertificateAuthorityArn" in data:
        out["certificate_authority_arn"] = data["CertificateAuthorityArn"]
    else:
        raise DeserializationError(
            "CreateCertificateAuthorityAuditReportRequest.certificate_authority_arn required"
        )
    if "S3BucketName" in data:
        out["s3_bucket_name"] = data["S3BucketName"]
    else:
        raise DeserializationError(
            "CreateCertificateAuthorityAuditReportRequest.s3_bucket_name required"
        )
    if "AuditReportResponseFormat" in data:
        import aws_sdk_acm_pca.types.audit_report_response_format

        out["audit_report_response_format"] = (
            aws_sdk_acm_pca.types.audit_report_response_format.deserialize_aws_json_1_1(
                data["AuditReportResponseFormat"]
            )
        )
    else:
        raise DeserializationError(
            "CreateCertificateAuthorityAuditReportRequest.audit_report_response_format required"
        )
    return out
