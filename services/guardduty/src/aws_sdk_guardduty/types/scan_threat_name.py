"""Generated from Smithy shape ``com.amazonaws.guardduty#ScanThreatName``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.file_paths
    import aws_sdk_guardduty.types.integer
    import aws_sdk_guardduty.types.string


class ScanThreatName(TypedDict, closed=True):
    name: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The name of the identified threat.</p>"""
    severity: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Severity of threat identified as part of the malware scan.</p>"""
    item_count: NotRequired["aws_sdk_guardduty.types.integer.Integer"]
    """<p>Total number of files infected with given threat.</p>"""
    file_paths: NotRequired["aws_sdk_guardduty.types.file_paths.FilePaths"]
    """<p>List of infected files in EBS volume with details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScanThreatName) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "severity" in value:
        out["severity"] = value["severity"]
    if "item_count" in value:
        out["itemCount"] = value["item_count"]
    if "file_paths" in value:
        import aws_sdk_guardduty.types.file_paths

        out["filePaths"] = aws_sdk_guardduty.types.file_paths.serialize_json(
            value["file_paths"]
        )
    return out


def deserialize_json(data: dict) -> ScanThreatName:
    out: ScanThreatName = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "severity" in data:
        out["severity"] = data["severity"]
    if "itemCount" in data:
        out["item_count"] = data["itemCount"]
    if "filePaths" in data:
        import aws_sdk_guardduty.types.file_paths

        out["file_paths"] = aws_sdk_guardduty.types.file_paths.deserialize_json(
            data["filePaths"]
        )
    return out
