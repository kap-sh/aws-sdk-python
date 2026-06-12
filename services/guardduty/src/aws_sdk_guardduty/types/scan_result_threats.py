"""Generated from Smithy shape ``com.amazonaws.guardduty#ScanResultThreats``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.scan_result_threat

ScanResultThreats: TypeAlias = list[
    "aws_sdk_guardduty.types.scan_result_threat.ScanResultThreat"
]


# --- restJson1 ser/de ---
def serialize_json(value: ScanResultThreats) -> list:
    import aws_sdk_guardduty.types.scan_result_threat

    out: list = []
    for item in value:
        out.append(aws_sdk_guardduty.types.scan_result_threat.serialize_json(item))
    return out


def deserialize_json(data: list) -> ScanResultThreats:
    import aws_sdk_guardduty.types.scan_result_threat

    out: ScanResultThreats = []
    for item in data:
        out.append(aws_sdk_guardduty.types.scan_result_threat.deserialize_json(item))
    return out
