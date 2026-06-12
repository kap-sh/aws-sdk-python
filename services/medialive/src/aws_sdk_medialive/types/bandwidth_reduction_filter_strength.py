"""Generated from Smithy shape ``com.amazonaws.medialive#BandwidthReductionFilterStrength``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Bandwidth Reduction Filter Strength"""
BandwidthReductionFilterStrength: TypeAlias = Literal[
    "AUTO",
    "STRENGTH_1",
    "STRENGTH_2",
    "STRENGTH_3",
    "STRENGTH_4",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO",
        "STRENGTH_1",
        "STRENGTH_2",
        "STRENGTH_3",
        "STRENGTH_4",
    )
)


def serialize_json(value: BandwidthReductionFilterStrength) -> str:
    return value


def deserialize_json(data: str) -> BandwidthReductionFilterStrength:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown BandwidthReductionFilterStrength value: {data!r}"
        )
    return cast(BandwidthReductionFilterStrength, data)
