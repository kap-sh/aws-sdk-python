"""Generated from Smithy shape ``com.amazonaws.acmpca#CreateCertificateAuthorityAuditReportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm_pca.types.audit_report_id
    import capo_acm_pca.types.s3_key


class CreateCertificateAuthorityAuditReportResponse(TypedDict, closed=True):
    audit_report_id: NotRequired["capo_acm_pca.types.audit_report_id.AuditReportId"]
    """<p>An alphanumeric string that contains a report identifier.</p>"""
    s3_key: NotRequired["capo_acm_pca.types.s3_key.S3Key"]
    """<p>The <b>key</b> that uniquely identifies the report file in your S3 bucket.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: CreateCertificateAuthorityAuditReportResponse,
) -> dict:
    out: dict = {}
    if "audit_report_id" in value:
        out["AuditReportId"] = value["audit_report_id"]
    if "s3_key" in value:
        out["S3Key"] = value["s3_key"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> CreateCertificateAuthorityAuditReportResponse:
    out: CreateCertificateAuthorityAuditReportResponse = {}  # type: ignore[typeddict-item]
    if "AuditReportId" in data:
        out["audit_report_id"] = data["AuditReportId"]
    if "S3Key" in data:
        out["s3_key"] = data["S3Key"]
    return out
