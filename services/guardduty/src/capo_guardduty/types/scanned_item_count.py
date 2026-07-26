"""Generated from Smithy shape ``com.amazonaws.guardduty#ScannedItemCount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.integer


class ScannedItemCount(TypedDict, closed=True):
    total_gb: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>Total GB of files scanned for malware.</p>"""
    files: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>Number of files scanned.</p>"""
    volumes: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>Total number of scanned volumes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScannedItemCount) -> dict:
    out: dict = {}
    if "total_gb" in value:
        out["totalGb"] = value["total_gb"]
    if "files" in value:
        out["files"] = value["files"]
    if "volumes" in value:
        out["volumes"] = value["volumes"]
    return out


def deserialize_json(data: dict) -> ScannedItemCount:
    out: ScannedItemCount = {}  # type: ignore[typeddict-item]
    if "totalGb" in data:
        out["total_gb"] = data["totalGb"]
    if "files" in data:
        out["files"] = data["files"]
    if "volumes" in data:
        out["volumes"] = data["volumes"]
    return out
