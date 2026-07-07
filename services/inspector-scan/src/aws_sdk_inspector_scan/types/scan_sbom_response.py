"""Generated from Smithy shape ``com.amazonaws.inspectorscan#ScanSbomResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector_scan.types.sbom


class ScanSbomResponse(TypedDict, closed=True):
    sbom: NotRequired["aws_sdk_inspector_scan.types.sbom.Sbom"]
    """<p>The vulnerability report for the scanned SBOM.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScanSbomResponse) -> dict:
    out: dict = {}
    if "sbom" in value:
        out["sbom"] = value["sbom"]
    return out


def deserialize_json(data: dict) -> ScanSbomResponse:
    out: ScanSbomResponse = {}  # type: ignore[typeddict-item]
    if "sbom" in data:
        out["sbom"] = data["sbom"]
    return out
