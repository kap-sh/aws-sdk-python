"""Generated from Smithy shape ``com.amazonaws.iot#ListCACertificatesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.ca_certificates
    import aws_sdk_iot.types.marker


class ListCACertificatesResponse(TypedDict):
    certificates: NotRequired["aws_sdk_iot.types.ca_certificates.CACertificates"]
    """<p>The CA certificates registered in your Amazon Web Services account.</p>"""
    next_marker: NotRequired["aws_sdk_iot.types.marker.Marker"]
    """<p>The current position within the list of CA certificates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCACertificatesResponse) -> dict:
    out: dict = {}
    if "certificates" in value:
        import aws_sdk_iot.types.ca_certificates

        out["certificates"] = aws_sdk_iot.types.ca_certificates.serialize_json(
            value["certificates"]
        )
    if "next_marker" in value:
        out["nextMarker"] = value["next_marker"]
    return out


def deserialize_json(data: dict) -> ListCACertificatesResponse:
    out: ListCACertificatesResponse = {}  # type: ignore[typeddict-item]
    if "certificates" in data:
        import aws_sdk_iot.types.ca_certificates

        out["certificates"] = aws_sdk_iot.types.ca_certificates.deserialize_json(
            data["certificates"]
        )
    if "nextMarker" in data:
        out["next_marker"] = data["nextMarker"]
    return out
