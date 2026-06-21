"""Generated from Smithy shape ``com.amazonaws.guardduty#IpSetFormat``."""

from typing import Literal, TypeAlias, cast

IpSetFormat: TypeAlias = Literal[
    "TXT",
    "STIX",
    "OTX_CSV",
    "ALIEN_VAULT",
    "PROOF_POINT",
    "FIRE_EYE",
]


# --- restJson1 ser/de ---
def serialize_json(value: IpSetFormat) -> str:
    return value


def deserialize_json(data: str) -> IpSetFormat:
    return cast(IpSetFormat, data)
