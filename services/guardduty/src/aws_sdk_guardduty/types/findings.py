"""Generated from Smithy shape ``com.amazonaws.guardduty#Findings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.finding

Findings: TypeAlias = list["aws_sdk_guardduty.types.finding.Finding"]


# --- restJson1 ser/de ---
def serialize_json(value: Findings) -> list:
    import aws_sdk_guardduty.types.finding

    out: list = []
    for item in value:
        out.append(aws_sdk_guardduty.types.finding.serialize_json(item))
    return out


def deserialize_json(data: list) -> Findings:
    import aws_sdk_guardduty.types.finding

    out: Findings = []
    for item in data:
        out.append(aws_sdk_guardduty.types.finding.deserialize_json(item))
    return out
