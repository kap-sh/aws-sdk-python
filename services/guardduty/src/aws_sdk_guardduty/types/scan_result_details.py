"""Generated from Smithy shape ``com.amazonaws.guardduty#ScanResultDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.scan_result


class ScanResultDetails(TypedDict):
    scan_result: NotRequired["aws_sdk_guardduty.types.scan_result.ScanResult"]
    """<p>An enum value representing possible scan results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScanResultDetails) -> dict:
    out: dict = {}
    if "scan_result" in value:
        import aws_sdk_guardduty.types.scan_result

        out["scanResult"] = aws_sdk_guardduty.types.scan_result.serialize_json(
            value["scan_result"]
        )
    return out


def deserialize_json(data: dict) -> ScanResultDetails:
    out: ScanResultDetails = {}  # type: ignore[typeddict-item]
    if "scanResult" in data:
        import aws_sdk_guardduty.types.scan_result

        out["scan_result"] = aws_sdk_guardduty.types.scan_result.deserialize_json(
            data["scanResult"]
        )
    return out
