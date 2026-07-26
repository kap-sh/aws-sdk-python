"""Generated from Smithy shape ``com.amazonaws.iot#IssuerCertificateIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.issuer_certificate_serial_number
    import capo_iot.types.issuer_certificate_subject
    import capo_iot.types.issuer_id


class IssuerCertificateIdentifier(TypedDict, closed=True):
    issuer_certificate_subject: NotRequired[
        "capo_iot.types.issuer_certificate_subject.IssuerCertificateSubject"
    ]
    """<p>The subject of the issuer certificate.</p>"""
    issuer_id: NotRequired["capo_iot.types.issuer_id.IssuerId"]
    """<p>The issuer ID.</p>"""
    issuer_certificate_serial_number: NotRequired[
        "capo_iot.types.issuer_certificate_serial_number.IssuerCertificateSerialNumber"
    ]
    """<p>The issuer certificate serial number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IssuerCertificateIdentifier) -> dict:
    out: dict = {}
    if "issuer_certificate_subject" in value:
        out["issuerCertificateSubject"] = value["issuer_certificate_subject"]
    if "issuer_id" in value:
        out["issuerId"] = value["issuer_id"]
    if "issuer_certificate_serial_number" in value:
        out["issuerCertificateSerialNumber"] = value["issuer_certificate_serial_number"]
    return out


def deserialize_json(data: dict) -> IssuerCertificateIdentifier:
    out: IssuerCertificateIdentifier = {}  # type: ignore[typeddict-item]
    if "issuerCertificateSubject" in data:
        out["issuer_certificate_subject"] = data["issuerCertificateSubject"]
    if "issuerId" in data:
        out["issuer_id"] = data["issuerId"]
    if "issuerCertificateSerialNumber" in data:
        out["issuer_certificate_serial_number"] = data["issuerCertificateSerialNumber"]
    return out
