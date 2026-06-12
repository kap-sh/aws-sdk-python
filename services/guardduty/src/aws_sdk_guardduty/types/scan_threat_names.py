"""Generated from Smithy shape ``com.amazonaws.guardduty#ScanThreatNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.scan_threat_name

ScanThreatNames: TypeAlias = list[
    "aws_sdk_guardduty.types.scan_threat_name.ScanThreatName"
]


# --- restJson1 ser/de ---
def serialize_json(value: ScanThreatNames) -> list:
    import aws_sdk_guardduty.types.scan_threat_name

    out: list = []
    for item in value:
        out.append(aws_sdk_guardduty.types.scan_threat_name.serialize_json(item))
    return out


def deserialize_json(data: list) -> ScanThreatNames:
    import aws_sdk_guardduty.types.scan_threat_name

    out: ScanThreatNames = []
    for item in data:
        out.append(aws_sdk_guardduty.types.scan_threat_name.deserialize_json(item))
    return out
