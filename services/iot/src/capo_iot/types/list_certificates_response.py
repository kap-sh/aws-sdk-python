"""Generated from Smithy shape ``com.amazonaws.iot#ListCertificatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.certificates
    import capo_iot.types.marker


class ListCertificatesResponse(TypedDict, closed=True):
    certificates: NotRequired["capo_iot.types.certificates.Certificates"]
    """<p>The descriptions of the certificates.</p>"""
    next_marker: NotRequired["capo_iot.types.marker.Marker"]
    """<p>The marker for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCertificatesResponse) -> dict:
    out: dict = {}
    if "certificates" in value:
        import capo_iot.types.certificates

        out["certificates"] = capo_iot.types.certificates.serialize_json(
            value["certificates"]
        )
    if "next_marker" in value:
        out["nextMarker"] = value["next_marker"]
    return out


def deserialize_json(data: dict) -> ListCertificatesResponse:
    out: ListCertificatesResponse = {}  # type: ignore[typeddict-item]
    if "certificates" in data:
        import capo_iot.types.certificates

        out["certificates"] = capo_iot.types.certificates.deserialize_json(
            data["certificates"]
        )
    if "nextMarker" in data:
        out["next_marker"] = data["nextMarker"]
    return out
