"""Generated from Smithy shape ``com.amazonaws.iot#ListOutgoingCertificatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.marker
    import capo_iot.types.outgoing_certificates


class ListOutgoingCertificatesResponse(TypedDict, closed=True):
    outgoing_certificates: NotRequired[
        "capo_iot.types.outgoing_certificates.OutgoingCertificates"
    ]
    """<p>The certificates that are being transferred but not yet accepted.</p>"""
    next_marker: NotRequired["capo_iot.types.marker.Marker"]
    """<p>The marker for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOutgoingCertificatesResponse) -> dict:
    out: dict = {}
    if "outgoing_certificates" in value:
        import capo_iot.types.outgoing_certificates

        out["outgoingCertificates"] = (
            capo_iot.types.outgoing_certificates.serialize_json(
                value["outgoing_certificates"]
            )
        )
    if "next_marker" in value:
        out["nextMarker"] = value["next_marker"]
    return out


def deserialize_json(data: dict) -> ListOutgoingCertificatesResponse:
    out: ListOutgoingCertificatesResponse = {}  # type: ignore[typeddict-item]
    if "outgoingCertificates" in data:
        import capo_iot.types.outgoing_certificates

        out["outgoing_certificates"] = (
            capo_iot.types.outgoing_certificates.deserialize_json(
                data["outgoingCertificates"]
            )
        )
    if "nextMarker" in data:
        out["next_marker"] = data["nextMarker"]
    return out
