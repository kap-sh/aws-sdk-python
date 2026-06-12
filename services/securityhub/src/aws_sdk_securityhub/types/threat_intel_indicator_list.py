"""Generated from Smithy shape ``com.amazonaws.securityhub#ThreatIntelIndicatorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.threat_intel_indicator

ThreatIntelIndicatorList: TypeAlias = list[
    "aws_sdk_securityhub.types.threat_intel_indicator.ThreatIntelIndicator"
]


# --- restJson1 ser/de ---
def serialize_json(value: ThreatIntelIndicatorList) -> list:
    import aws_sdk_securityhub.types.threat_intel_indicator

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.threat_intel_indicator.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ThreatIntelIndicatorList:
    import aws_sdk_securityhub.types.threat_intel_indicator

    out: ThreatIntelIndicatorList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.threat_intel_indicator.deserialize_json(item)
        )
    return out
