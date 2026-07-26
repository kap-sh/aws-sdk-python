"""Generated from Smithy shape ``com.amazonaws.securityhub#ThreatIntelIndicatorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.threat_intel_indicator

ThreatIntelIndicatorList: TypeAlias = list[
    "capo_securityhub.types.threat_intel_indicator.ThreatIntelIndicator"
]


# --- restJson1 ser/de ---
def serialize_json(value: ThreatIntelIndicatorList) -> list:
    import capo_securityhub.types.threat_intel_indicator

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.threat_intel_indicator.serialize_json(item))
    return out


def deserialize_json(data: list) -> ThreatIntelIndicatorList:
    import capo_securityhub.types.threat_intel_indicator

    out: ThreatIntelIndicatorList = []
    for item in data:
        out.append(capo_securityhub.types.threat_intel_indicator.deserialize_json(item))
    return out
