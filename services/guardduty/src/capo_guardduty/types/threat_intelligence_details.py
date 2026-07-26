"""Generated from Smithy shape ``com.amazonaws.guardduty#ThreatIntelligenceDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.threat_intelligence_detail

ThreatIntelligenceDetails: TypeAlias = list[
    "capo_guardduty.types.threat_intelligence_detail.ThreatIntelligenceDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: ThreatIntelligenceDetails) -> list:
    import capo_guardduty.types.threat_intelligence_detail

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.threat_intelligence_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> ThreatIntelligenceDetails:
    import capo_guardduty.types.threat_intelligence_detail

    out: ThreatIntelligenceDetails = []
    for item in data:
        out.append(
            capo_guardduty.types.threat_intelligence_detail.deserialize_json(item)
        )
    return out
