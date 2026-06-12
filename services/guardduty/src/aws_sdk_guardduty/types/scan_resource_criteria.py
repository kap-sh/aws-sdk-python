"""Generated from Smithy shape ``com.amazonaws.guardduty#ScanResourceCriteria``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.scan_criterion


class ScanResourceCriteria(TypedDict):
    include: NotRequired["aws_sdk_guardduty.types.scan_criterion.ScanCriterion"]
    """<p>Represents condition that when matched will allow a malware scan for a certain resource.</p>"""
    exclude: NotRequired["aws_sdk_guardduty.types.scan_criterion.ScanCriterion"]
    """<p>Represents condition that when matched will prevent a malware scan for a certain resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScanResourceCriteria) -> dict:
    out: dict = {}
    if "include" in value:
        import aws_sdk_guardduty.types.scan_criterion

        out["include"] = aws_sdk_guardduty.types.scan_criterion.serialize_json(
            value["include"]
        )
    if "exclude" in value:
        import aws_sdk_guardduty.types.scan_criterion

        out["exclude"] = aws_sdk_guardduty.types.scan_criterion.serialize_json(
            value["exclude"]
        )
    return out


def deserialize_json(data: dict) -> ScanResourceCriteria:
    out: ScanResourceCriteria = {}  # type: ignore[typeddict-item]
    if "include" in data:
        import aws_sdk_guardduty.types.scan_criterion

        out["include"] = aws_sdk_guardduty.types.scan_criterion.deserialize_json(
            data["include"]
        )
    if "exclude" in data:
        import aws_sdk_guardduty.types.scan_criterion

        out["exclude"] = aws_sdk_guardduty.types.scan_criterion.deserialize_json(
            data["exclude"]
        )
    return out
