"""Generated from Smithy shape ``com.amazonaws.guardduty#ThreatIntelSetFormat``."""

from typing import Literal, TypeAlias, cast

ThreatIntelSetFormat: TypeAlias = Literal[
    "TXT",
    "STIX",
    "OTX_CSV",
    "ALIEN_VAULT",
    "PROOF_POINT",
    "FIRE_EYE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ThreatIntelSetFormat) -> str:
    return value


def deserialize_json(data: str) -> ThreatIntelSetFormat:
    return cast(ThreatIntelSetFormat, data)
