"""Generated from Smithy shape ``com.amazonaws.backup#ScanFindings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backup.types.scan_finding

ScanFindings: TypeAlias = list["aws_sdk_backup.types.scan_finding.ScanFinding"]


# --- restJson1 ser/de ---
def serialize_json(value: ScanFindings) -> list:
    import aws_sdk_backup.types.scan_finding

    out: list = []
    for item in value:
        out.append(aws_sdk_backup.types.scan_finding.serialize_json(item))
    return out


def deserialize_json(data: list) -> ScanFindings:
    import aws_sdk_backup.types.scan_finding

    out: ScanFindings = []
    for item in data:
        out.append(aws_sdk_backup.types.scan_finding.deserialize_json(item))
    return out
