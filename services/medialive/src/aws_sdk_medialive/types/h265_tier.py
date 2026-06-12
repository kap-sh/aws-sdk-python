"""Generated from Smithy shape ``com.amazonaws.medialive#H265Tier``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H265 Tier"""
H265Tier: TypeAlias = Literal[
    "HIGH",
    "MAIN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HIGH",
        "MAIN",
    )
)


def serialize_json(value: H265Tier) -> str:
    return value


def deserialize_json(data: str) -> H265Tier:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H265Tier value: {data!r}")
    return cast(H265Tier, data)
