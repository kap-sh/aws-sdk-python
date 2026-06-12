"""Generated from Smithy shape ``com.amazonaws.transfer#UpdateCertificateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.cert_date
    import aws_sdk_transfer.types.certificate_id
    import aws_sdk_transfer.types.description


class UpdateCertificateRequest(TypedDict):
    certificate_id: "aws_sdk_transfer.types.certificate_id.CertificateId"
    """<p>The identifier of the certificate object that you are updating.</p>"""
    active_date: NotRequired["aws_sdk_transfer.types.cert_date.CertDate"]
    """<p>An optional date that specifies when the certificate becomes active. If you do not specify a value, <code>ActiveDate</code> takes the same value as <code>NotBeforeDate</code>, which is specified by the CA. </p>"""
    inactive_date: NotRequired["aws_sdk_transfer.types.cert_date.CertDate"]
    """<p>An optional date that specifies when the certificate becomes inactive. If you do not specify a value, <code>InactiveDate</code> takes the same value as <code>NotAfterDate</code>, which is specified by the CA.</p>"""
    description: NotRequired["aws_sdk_transfer.types.description.Description"]
    """<p>A short description to help identify the certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCertificateRequest) -> dict:
    out: dict = {}
    out["CertificateId"] = value["certificate_id"]
    if "active_date" in value:
        import aws_sdk_transfer.types.cert_date

        out["ActiveDate"] = aws_sdk_transfer.types.cert_date.serialize_aws_json_1_1(
            value["active_date"]
        )
    if "inactive_date" in value:
        import aws_sdk_transfer.types.cert_date

        out["InactiveDate"] = aws_sdk_transfer.types.cert_date.serialize_aws_json_1_1(
            value["inactive_date"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateCertificateRequest:
    out: UpdateCertificateRequest = {}  # type: ignore[typeddict-item]
    if "CertificateId" in data:
        out["certificate_id"] = data["CertificateId"]
    else:
        raise DeserializationError("UpdateCertificateRequest.certificate_id required")
    if "ActiveDate" in data:
        import aws_sdk_transfer.types.cert_date

        out["active_date"] = aws_sdk_transfer.types.cert_date.deserialize_aws_json_1_1(
            data["ActiveDate"]
        )
    if "InactiveDate" in data:
        import aws_sdk_transfer.types.cert_date

        out["inactive_date"] = (
            aws_sdk_transfer.types.cert_date.deserialize_aws_json_1_1(
                data["InactiveDate"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    return out
