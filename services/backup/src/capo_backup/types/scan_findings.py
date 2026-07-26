"""Generated from Smithy shape ``com.amazonaws.backup#ScanFindings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.scan_finding

ScanFindings: TypeAlias = list["capo_backup.types.scan_finding.ScanFinding"]


# --- restJson1 ser/de ---
def serialize_json(value: ScanFindings) -> list:
    import capo_backup.types.scan_finding

    out: list = []
    for item in value:
        out.append(capo_backup.types.scan_finding.serialize_json(item))
    return out


def deserialize_json(data: list) -> ScanFindings:
    import capo_backup.types.scan_finding

    out: ScanFindings = []
    for item in data:
        out.append(capo_backup.types.scan_finding.deserialize_json(item))
    return out
