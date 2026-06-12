"""Generated from Smithy shape ``com.amazonaws.iot#ListCertificatesByCAResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.certificates
    import aws_sdk_iot.types.marker


class ListCertificatesByCAResponse(TypedDict):
    certificates: NotRequired["aws_sdk_iot.types.certificates.Certificates"]
    """<p>The device certificates signed by the specified CA certificate.</p>"""
    next_marker: NotRequired["aws_sdk_iot.types.marker.Marker"]
    """<p>The marker for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCertificatesByCAResponse) -> dict:
    out: dict = {}
    if "certificates" in value:
        import aws_sdk_iot.types.certificates

        out["certificates"] = aws_sdk_iot.types.certificates.serialize_json(
            value["certificates"]
        )
    if "next_marker" in value:
        out["nextMarker"] = value["next_marker"]
    return out


def deserialize_json(data: dict) -> ListCertificatesByCAResponse:
    out: ListCertificatesByCAResponse = {}  # type: ignore[typeddict-item]
    if "certificates" in data:
        import aws_sdk_iot.types.certificates

        out["certificates"] = aws_sdk_iot.types.certificates.deserialize_json(
            data["certificates"]
        )
    if "nextMarker" in data:
        out["next_marker"] = data["nextMarker"]
    return out
