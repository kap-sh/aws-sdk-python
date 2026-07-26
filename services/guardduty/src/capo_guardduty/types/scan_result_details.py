"""Generated from Smithy shape ``com.amazonaws.guardduty#ScanResultDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.scan_result


class ScanResultDetails(TypedDict, closed=True):
    scan_result: NotRequired["capo_guardduty.types.scan_result.ScanResult"]
    """<p>An enum value representing possible scan results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScanResultDetails) -> dict:
    out: dict = {}
    if "scan_result" in value:
        import capo_guardduty.types.scan_result

        out["scanResult"] = capo_guardduty.types.scan_result.serialize_json(
            value["scan_result"]
        )
    return out


def deserialize_json(data: dict) -> ScanResultDetails:
    out: ScanResultDetails = {}  # type: ignore[typeddict-item]
    if "scanResult" in data:
        import capo_guardduty.types.scan_result

        out["scan_result"] = capo_guardduty.types.scan_result.deserialize_json(
            data["scanResult"]
        )
    return out
