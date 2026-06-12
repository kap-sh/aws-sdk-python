"""Generated from Smithy shape ``com.amazonaws.medialive#BandwidthReductionPostFilterSharpening``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Bandwidth Reduction Post Filter Sharpening"""
BandwidthReductionPostFilterSharpening: TypeAlias = Literal[
    "DISABLED",
    "SHARPENING_1",
    "SHARPENING_2",
    "SHARPENING_3",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "SHARPENING_1",
        "SHARPENING_2",
        "SHARPENING_3",
    )
)


def serialize_json(value: BandwidthReductionPostFilterSharpening) -> str:
    return value


def deserialize_json(data: str) -> BandwidthReductionPostFilterSharpening:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown BandwidthReductionPostFilterSharpening value: {data!r}"
        )
    return cast(BandwidthReductionPostFilterSharpening, data)
