"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#CredentialSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime


class CredentialSummary(TypedDict, closed=True):
    seen_at: NotRequired["datetime.datetime"]
    """<p>The ISO-8601 time stamp of when the certificate was last used in a temporary credential request.</p>"""
    serial_number: NotRequired["str"]
    """<p>The serial number of the certificate.</p>"""
    issuer: NotRequired["str"]
    """<p>The fully qualified domain name of the issuing certificate for the presented end-entity certificate.</p>"""
    enabled: NotRequired["bool"]
    """<p>Indicates whether the credential is enabled.</p>"""
    x509_certificate_data: NotRequired["str"]
    """<p>The PEM-encoded data of the certificate.</p>"""
    failed: NotRequired["bool"]
    """<p>Indicates whether the temporary credential request was successful. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CredentialSummary) -> dict:
    out: dict = {}
    if "seen_at" in value:
        import aws_sdk_rolesanywhere.types._prelude.timestamp

        out["seenAt"] = aws_sdk_rolesanywhere.types._prelude.timestamp.serialize_json(
            value["seen_at"]
        )
    if "serial_number" in value:
        out["serialNumber"] = value["serial_number"]
    if "issuer" in value:
        out["issuer"] = value["issuer"]
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "x509_certificate_data" in value:
        out["x509CertificateData"] = value["x509_certificate_data"]
    if "failed" in value:
        out["failed"] = value["failed"]
    return out


def deserialize_json(data: dict) -> CredentialSummary:
    out: CredentialSummary = {}  # type: ignore[typeddict-item]
    if "seenAt" in data:
        import aws_sdk_rolesanywhere.types._prelude.timestamp

        out["seen_at"] = (
            aws_sdk_rolesanywhere.types._prelude.timestamp.deserialize_json(
                data["seenAt"]
            )
        )
    if "serialNumber" in data:
        out["serial_number"] = data["serialNumber"]
    if "issuer" in data:
        out["issuer"] = data["issuer"]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    if "x509CertificateData" in data:
        out["x509_certificate_data"] = data["x509CertificateData"]
    if "failed" in data:
        out["failed"] = data["failed"]
    return out
