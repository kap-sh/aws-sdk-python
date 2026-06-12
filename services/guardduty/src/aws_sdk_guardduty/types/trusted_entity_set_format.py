"""Generated from Smithy shape ``com.amazonaws.guardduty#TrustedEntitySetFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

TrustedEntitySetFormat: TypeAlias = Literal[
    "TXT",
    "STIX",
    "OTX_CSV",
    "ALIEN_VAULT",
    "PROOF_POINT",
    "FIRE_EYE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TXT",
        "STIX",
        "OTX_CSV",
        "ALIEN_VAULT",
        "PROOF_POINT",
        "FIRE_EYE",
    )
)


def serialize_json(value: TrustedEntitySetFormat) -> str:
    return value


def deserialize_json(data: str) -> TrustedEntitySetFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TrustedEntitySetFormat value: {data!r}")
    return cast(TrustedEntitySetFormat, data)
