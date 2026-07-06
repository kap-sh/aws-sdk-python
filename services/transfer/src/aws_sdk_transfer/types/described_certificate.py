"""Generated from Smithy shape ``com.amazonaws.transfer#DescribedCertificate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.arn
    import aws_sdk_transfer.types.cert_date
    import aws_sdk_transfer.types.cert_serial
    import aws_sdk_transfer.types.certificate_body_type
    import aws_sdk_transfer.types.certificate_chain_type
    import aws_sdk_transfer.types.certificate_id
    import aws_sdk_transfer.types.certificate_status_type
    import aws_sdk_transfer.types.certificate_type
    import aws_sdk_transfer.types.certificate_usage_type
    import aws_sdk_transfer.types.description
    import aws_sdk_transfer.types.tags


class DescribedCertificate(TypedDict, closed=True):
    arn: "aws_sdk_transfer.types.arn.Arn"
    """<p>The unique Amazon Resource Name (ARN) for the certificate.</p>"""
    certificate_id: NotRequired["aws_sdk_transfer.types.certificate_id.CertificateId"]
    """<p>An array of identifiers for the imported certificates. You use this identifier for working with profiles and partner profiles.</p>"""
    usage: NotRequired[
        "aws_sdk_transfer.types.certificate_usage_type.CertificateUsageType"
    ]
    """<p>Specifies how this certificate is used. It can be used in the following ways:</p> <ul> <li> <p> <code>SIGNING</code>: For signing AS2 messages</p> </li> <li> <p> <code>ENCRYPTION</code>: For encrypting AS2 messages</p> </li> <li> <p> <code>TLS</code>: For securing AS2 communications sent over HTTPS</p> </li> </ul>"""
    status: NotRequired[
        "aws_sdk_transfer.types.certificate_status_type.CertificateStatusType"
    ]
    """<p>A certificate's status can be either <code>ACTIVE</code> or <code>INACTIVE</code>.</p> <p>You can set <code>ActiveDate</code> and <code>InactiveDate</code> in the <code>UpdateCertificate</code> call. If you set values for these parameters, those values are used to determine whether the certificate has a status of <code>ACTIVE</code> or <code>INACTIVE</code>.</p> <p>If you don't set values for <code>ActiveDate</code> and <code>InactiveDate</code>, we use the <code>NotBefore</code> and <code>NotAfter</code> date as specified on the X509 certificate to determine when a certificate is active and when it is inactive.</p>"""
    certificate: NotRequired[
        "aws_sdk_transfer.types.certificate_body_type.CertificateBodyType"
    ]
    """<p>The file name for the certificate.</p>"""
    certificate_chain: NotRequired[
        "aws_sdk_transfer.types.certificate_chain_type.CertificateChainType"
    ]
    """<p>The list of certificates that make up the chain for the certificate.</p>"""
    active_date: NotRequired["aws_sdk_transfer.types.cert_date.CertDate"]
    """<p>An optional date that specifies when the certificate becomes active. If you do not specify a value, <code>ActiveDate</code> takes the same value as <code>NotBeforeDate</code>, which is specified by the CA. </p>"""
    inactive_date: NotRequired["aws_sdk_transfer.types.cert_date.CertDate"]
    """<p>An optional date that specifies when the certificate becomes inactive. If you do not specify a value, <code>InactiveDate</code> takes the same value as <code>NotAfterDate</code>, which is specified by the CA.</p>"""
    serial: NotRequired["aws_sdk_transfer.types.cert_serial.CertSerial"]
    """<p>The serial number for the certificate.</p>"""
    not_before_date: NotRequired["aws_sdk_transfer.types.cert_date.CertDate"]
    """<p>The earliest date that the certificate is valid.</p>"""
    not_after_date: NotRequired["aws_sdk_transfer.types.cert_date.CertDate"]
    """<p>The final date that the certificate is valid.</p>"""
    type: NotRequired["aws_sdk_transfer.types.certificate_type.CertificateType"]
    """<p>If a private key has been specified for the certificate, its type is <code>CERTIFICATE_WITH_PRIVATE_KEY</code>. If there is no private key, the type is <code>CERTIFICATE</code>.</p>"""
    description: NotRequired["aws_sdk_transfer.types.description.Description"]
    """<p>The name or description that's used to identity the certificate. </p>"""
    tags: NotRequired["aws_sdk_transfer.types.tags.Tags"]
    """<p>Key-value pairs that can be used to group and search for certificates.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribedCertificate) -> dict:
    out: dict = {}
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
    if "certificate" in value:
        out["Certificate"] = value["certificate"]
    if "certificate_chain" in value:
        out["CertificateChain"] = value["certificate_chain"]
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
    if "serial" in value:
        out["Serial"] = value["serial"]
    if "not_before_date" in value:
        import aws_sdk_transfer.types.cert_date

        out["NotBeforeDate"] = aws_sdk_transfer.types.cert_date.serialize_aws_json_1_1(
            value["not_before_date"]
        )
    if "not_after_date" in value:
        import aws_sdk_transfer.types.cert_date

        out["NotAfterDate"] = aws_sdk_transfer.types.cert_date.serialize_aws_json_1_1(
            value["not_after_date"]
        )
    if "type" in value:
        import aws_sdk_transfer.types.certificate_type

        out["Type"] = aws_sdk_transfer.types.certificate_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import aws_sdk_transfer.types.tags

        out["Tags"] = aws_sdk_transfer.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribedCertificate:
    out: DescribedCertificate = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("DescribedCertificate.arn required")
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
    if "Certificate" in data:
        out["certificate"] = data["Certificate"]
    if "CertificateChain" in data:
        out["certificate_chain"] = data["CertificateChain"]
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
    if "Serial" in data:
        out["serial"] = data["Serial"]
    if "NotBeforeDate" in data:
        import aws_sdk_transfer.types.cert_date

        out["not_before_date"] = (
            aws_sdk_transfer.types.cert_date.deserialize_aws_json_1_1(
                data["NotBeforeDate"]
            )
        )
    if "NotAfterDate" in data:
        import aws_sdk_transfer.types.cert_date

        out["not_after_date"] = (
            aws_sdk_transfer.types.cert_date.deserialize_aws_json_1_1(
                data["NotAfterDate"]
            )
        )
    if "Type" in data:
        import aws_sdk_transfer.types.certificate_type

        out["type"] = aws_sdk_transfer.types.certificate_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Tags" in data:
        import aws_sdk_transfer.types.tags

        out["tags"] = aws_sdk_transfer.types.tags.deserialize_aws_json_1_1(data["Tags"])
    return out
