"""Generated from Smithy shape ``com.amazonaws.iot#CACertificate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.ca_certificate_status
    import aws_sdk_iot.types.certificate_arn
    import aws_sdk_iot.types.certificate_id
    import aws_sdk_iot.types.date_type


class CACertificate(TypedDict):
    certificate_arn: NotRequired["aws_sdk_iot.types.certificate_arn.CertificateArn"]
    """<p>The ARN of the CA certificate.</p>"""
    certificate_id: NotRequired["aws_sdk_iot.types.certificate_id.CertificateId"]
    """<p>The ID of the CA certificate.</p>"""
    status: NotRequired["aws_sdk_iot.types.ca_certificate_status.CACertificateStatus"]
    """<p>The status of the CA certificate.</p> <p>The status value REGISTER_INACTIVE is deprecated and should not be used.</p>"""
    creation_date: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The date the CA certificate was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CACertificate) -> dict:
    out: dict = {}
    if "certificate_arn" in value:
        out["certificateArn"] = value["certificate_arn"]
    if "certificate_id" in value:
        out["certificateId"] = value["certificate_id"]
    if "status" in value:
        import aws_sdk_iot.types.ca_certificate_status

        out["status"] = aws_sdk_iot.types.ca_certificate_status.serialize_json(
            value["status"]
        )
    if "creation_date" in value:
        import aws_sdk_iot.types.date_type

        out["creationDate"] = aws_sdk_iot.types.date_type.serialize_json(
            value["creation_date"]
        )
    return out


def deserialize_json(data: dict) -> CACertificate:
    out: CACertificate = {}  # type: ignore[typeddict-item]
    if "certificateArn" in data:
        out["certificate_arn"] = data["certificateArn"]
    if "certificateId" in data:
        out["certificate_id"] = data["certificateId"]
    if "status" in data:
        import aws_sdk_iot.types.ca_certificate_status

        out["status"] = aws_sdk_iot.types.ca_certificate_status.deserialize_json(
            data["status"]
        )
    if "creationDate" in data:
        import aws_sdk_iot.types.date_type

        out["creation_date"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["creationDate"]
        )
    return out
