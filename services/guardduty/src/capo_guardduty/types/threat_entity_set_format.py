"""Generated from Smithy shape ``com.amazonaws.guardduty#ThreatEntitySetFormat``."""

from typing import Literal, TypeAlias, cast

ThreatEntitySetFormat: TypeAlias = Literal[
    "TXT",
    "STIX",
    "OTX_CSV",
    "ALIEN_VAULT",
    "PROOF_POINT",
    "FIRE_EYE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ThreatEntitySetFormat) -> str:
    return value


def deserialize_json(data: str) -> ThreatEntitySetFormat:
    return cast(ThreatEntitySetFormat, data)
