"""Generated from Smithy shape ``com.amazonaws.guardduty#FilePaths``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.scan_file_path

FilePaths: TypeAlias = list["capo_guardduty.types.scan_file_path.ScanFilePath"]


# --- restJson1 ser/de ---
def serialize_json(value: FilePaths) -> list:
    import capo_guardduty.types.scan_file_path

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.scan_file_path.serialize_json(item))
    return out


def deserialize_json(data: list) -> FilePaths:
    import capo_guardduty.types.scan_file_path

    out: FilePaths = []
    for item in data:
        out.append(capo_guardduty.types.scan_file_path.deserialize_json(item))
    return out
