"""Generated from Smithy shape ``com.amazonaws.guardduty#ScanFilePath``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string


class ScanFilePath(TypedDict, closed=True):
    file_path: NotRequired["capo_guardduty.types.string.String"]
    """<p>The file path of the infected file.</p>"""
    volume_arn: NotRequired["capo_guardduty.types.string.String"]
    """<p>EBS volume ARN details of the infected file.</p>"""
    hash: NotRequired["capo_guardduty.types.string.String"]
    """<p>The hash value of the infected file.</p>"""
    file_name: NotRequired["capo_guardduty.types.string.String"]
    """<p>File name of the infected file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScanFilePath) -> dict:
    out: dict = {}
    if "file_path" in value:
        out["filePath"] = value["file_path"]
    if "volume_arn" in value:
        out["volumeArn"] = value["volume_arn"]
    if "hash" in value:
        out["hash"] = value["hash"]
    if "file_name" in value:
        out["fileName"] = value["file_name"]
    return out


def deserialize_json(data: dict) -> ScanFilePath:
    out: ScanFilePath = {}  # type: ignore[typeddict-item]
    if "filePath" in data:
        out["file_path"] = data["filePath"]
    if "volumeArn" in data:
        out["volume_arn"] = data["volumeArn"]
    if "hash" in data:
        out["hash"] = data["hash"]
    if "fileName" in data:
        out["file_name"] = data["fileName"]
    return out
