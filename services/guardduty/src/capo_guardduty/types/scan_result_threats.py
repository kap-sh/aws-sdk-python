"""Generated from Smithy shape ``com.amazonaws.guardduty#ScanResultThreats``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.scan_result_threat

ScanResultThreats: TypeAlias = list[
    "capo_guardduty.types.scan_result_threat.ScanResultThreat"
]


# --- restJson1 ser/de ---
def serialize_json(value: ScanResultThreats) -> list:
    import capo_guardduty.types.scan_result_threat

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.scan_result_threat.serialize_json(item))
    return out


def deserialize_json(data: list) -> ScanResultThreats:
    import capo_guardduty.types.scan_result_threat

    out: ScanResultThreats = []
    for item in data:
        out.append(capo_guardduty.types.scan_result_threat.deserialize_json(item))
    return out
