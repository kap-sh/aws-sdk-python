"""Generated from Smithy shape ``com.amazonaws.guardduty#Findings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.finding

Findings: TypeAlias = list["capo_guardduty.types.finding.Finding"]


# --- restJson1 ser/de ---
def serialize_json(value: Findings) -> list:
    import capo_guardduty.types.finding

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.finding.serialize_json(item))
    return out


def deserialize_json(data: list) -> Findings:
    import capo_guardduty.types.finding

    out: Findings = []
    for item in data:
        out.append(capo_guardduty.types.finding.deserialize_json(item))
    return out
