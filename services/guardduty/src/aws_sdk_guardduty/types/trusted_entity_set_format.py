"""Generated from Smithy shape ``com.amazonaws.guardduty#TrustedEntitySetFormat``."""

from typing import Literal, TypeAlias, cast

TrustedEntitySetFormat: TypeAlias = Literal[
    "TXT",
    "STIX",
    "OTX_CSV",
    "ALIEN_VAULT",
    "PROOF_POINT",
    "FIRE_EYE",
]


# --- restJson1 ser/de ---
def serialize_json(value: TrustedEntitySetFormat) -> str:
    return value


def deserialize_json(data: str) -> TrustedEntitySetFormat:
    return cast(TrustedEntitySetFormat, data)
