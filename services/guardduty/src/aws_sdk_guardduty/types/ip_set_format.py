"""Generated from Smithy shape ``com.amazonaws.guardduty#IpSetFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

IpSetFormat: TypeAlias = Literal[
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


def serialize_json(value: IpSetFormat) -> str:
    return value


def deserialize_json(data: str) -> IpSetFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IpSetFormat value: {data!r}")
    return cast(IpSetFormat, data)
