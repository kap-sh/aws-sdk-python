"""Generated from Smithy shape ``com.amazonaws.transfer#ListedCertificate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transfer.types.arn
    import aws_sdk_transfer.types.cert_date
    import aws_sdk_transfer.types.certificate_id
    import aws_sdk_transfer.types.certificate_status_type
    import aws_sdk_transfer.types.certificate_type
    import aws_sdk_transfer.types.certificate_usage_type
    import aws_sdk_transfer.types.description


class ListedCertificate(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_transfer.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the specified certificate.</p>"""
    certificate_id: NotRequired["aws_sdk_transfer.types.certificate_id.CertificateId"]
    """<p>An array of identifiers for the imported certificates. You use this identifier for working with profiles and partner profiles.</p>"""
    usage: NotRequired[
        "aws_sdk_transfer.types.certificate_usage_type.CertificateUsageType"
    ]
    """<p>Specifies how this certificate is used. It can be used in the following ways:</p> <ul> <li> <p> <code>SIGNING</code>: For signing AS2 messages</p> </li> <li> <p> <code>ENCRYPTION</code>: For encrypting AS2 messages</p> </li> <li> <p> <code>TLS</code>: For securing AS2 communications sent over HTTPS</p> </li> </ul>"""
    status: NotRequired[
        "aws_sdk_transfer.types.certificate_status_type.CertificateStatusType"
    ]
    """<p>The certificate can be either <code>ACTIVE</code>, <code>PENDING_ROTATION</code>, or <code>INACTIVE</code>. <code>PENDING_ROTATION</code> means that this certificate will replace the current certificate when it expires.</p>"""
    active_date: NotRequired["aws_sdk_transfer.types.cert_date.CertDate"]
    """<p>An optional date that specifies when the certificate becomes active. If you do not specify a value, <code>ActiveDate</code> takes the same value as <code>NotBeforeDate</code>, which is specified by the CA. </p>"""
    inactive_date: NotRequired["aws_sdk_transfer.types.cert_date.CertDate"]
    """<p>An optional date that specifies when the certificate becomes inactive. If you do not specify a value, <code>InactiveDate</code> takes the same value as <code>NotAfterDate</code>, which is specified by the CA.</p>"""
    type: NotRequired["aws_sdk_transfer.types.certificate_type.CertificateType"]
    """<p>The type for the certificate. If a private key has been specified for the certificate, its type is <code>CERTIFICATE_WITH_PRIVATE_KEY</code>. If there is no private key, the type is <code>CERTIFICATE</code>.</p>"""
    description: NotRequired["aws_sdk_transfer.types.description.Description"]
    """<p>The name or short description that's used to identify the certificate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListedCertificate) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "certificate_id" in value:
        out["CertificateId"] = value["certificate_id"]
    if "usage" in value:
        import aws_sdk_transfer.types.certificate_usage_type

        out["Usage"] = (
            aws_sdk_transfer.types.certificate_usage_type.serialize_aws_json_1_1(
                value["usage"]
            )
        )
    if "status" in value:
        import aws_sdk_transfer.types.certificate_status_type

        out["Status"] = (
            aws_sdk_transfer.types.certificate_status_type.serialize_aws_json_1_1(
                value["status"]
            )
        )
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
    if "type" in value:
        import aws_sdk_transfer.types.certificate_type

        out["Type"] = aws_sdk_transfer.types.certificate_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListedCertificate:
    out: ListedCertificate = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "CertificateId" in data:
        out["certificate_id"] = data["CertificateId"]
    if "Usage" in data:
        import aws_sdk_transfer.types.certificate_usage_type

        out["usage"] = (
            aws_sdk_transfer.types.certificate_usage_type.deserialize_aws_json_1_1(
                data["Usage"]
            )
        )
    if "Status" in data:
        import aws_sdk_transfer.types.certificate_status_type

        out["status"] = (
            aws_sdk_transfer.types.certificate_status_type.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
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
    if "Type" in data:
        import aws_sdk_transfer.types.certificate_type

        out["type"] = aws_sdk_transfer.types.certificate_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    return out
