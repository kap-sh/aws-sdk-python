"""Generated from Smithy shape ``com.amazonaws.guardduty#Scans``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.scan

Scans: TypeAlias = list["aws_sdk_guardduty.types.scan.Scan"]


# --- restJson1 ser/de ---
def serialize_json(value: Scans) -> list:
    import aws_sdk_guardduty.types.scan

    out: list = []
    for item in value:
        out.append(aws_sdk_guardduty.types.scan.serialize_json(item))
    return out


def deserialize_json(data: list) -> Scans:
    import aws_sdk_guardduty.types.scan

    out: Scans = []
    for item in data:
        out.append(aws_sdk_guardduty.types.scan.deserialize_json(item))
    return out
