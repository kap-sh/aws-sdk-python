"""Generated from Smithy shape ``com.amazonaws.backup#ScanResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backup.types.scan_result

ScanResults: TypeAlias = list["aws_sdk_backup.types.scan_result.ScanResult"]


# --- restJson1 ser/de ---
def serialize_json(value: ScanResults) -> list:
    import aws_sdk_backup.types.scan_result

    out: list = []
    for item in value:
        out.append(aws_sdk_backup.types.scan_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> ScanResults:
    import aws_sdk_backup.types.scan_result

    out: ScanResults = []
    for item in data:
        out.append(aws_sdk_backup.types.scan_result.deserialize_json(item))
    return out
