"""Generated from Smithy shape ``com.amazonaws.iot#CACertificate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.ca_certificate_status
    import capo_iot.types.certificate_arn
    import capo_iot.types.certificate_id
    import capo_iot.types.date_type


class CACertificate(TypedDict, closed=True):
    certificate_arn: NotRequired["capo_iot.types.certificate_arn.CertificateArn"]
    """<p>The ARN of the CA certificate.</p>"""
    certificate_id: NotRequired["capo_iot.types.certificate_id.CertificateId"]
    """<p>The ID of the CA certificate.</p>"""
    status: NotRequired["capo_iot.types.ca_certificate_status.CACertificateStatus"]
    """<p>The status of the CA certificate.</p> <p>The status value REGISTER_INACTIVE is deprecated and should not be used.</p>"""
    creation_date: NotRequired["capo_iot.types.date_type.DateType"]
    """<p>The date the CA certificate was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CACertificate) -> dict:
    out: dict = {}
    if "certificate_arn" in value:
        out["certificateArn"] = value["certificate_arn"]
    if "certificate_id" in value:
        out["certificateId"] = value["certificate_id"]
    if "status" in value:
        import capo_iot.types.ca_certificate_status

        out["status"] = capo_iot.types.ca_certificate_status.serialize_json(
            value["status"]
        )
    if "creation_date" in value:
        import capo_iot.types.date_type

        out["creationDate"] = capo_iot.types.date_type.serialize_json(
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
        import capo_iot.types.ca_certificate_status

        out["status"] = capo_iot.types.ca_certificate_status.deserialize_json(
            data["status"]
        )
    if "creationDate" in data:
        import capo_iot.types.date_type

        out["creation_date"] = capo_iot.types.date_type.deserialize_json(
            data["creationDate"]
        )
    return out
