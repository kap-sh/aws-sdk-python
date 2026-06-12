"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H265AlternateTransferFunctionSei``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Enables Alternate Transfer Function SEI message for outputs using Hybrid Log Gamma (HLG) Electro-Optical Transfer Function (EOTF)."""
H265AlternateTransferFunctionSei: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
    )
)


def serialize_json(value: H265AlternateTransferFunctionSei) -> str:
    return value


def deserialize_json(data: str) -> H265AlternateTransferFunctionSei:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown H265AlternateTransferFunctionSei value: {data!r}"
        )
    return cast(H265AlternateTransferFunctionSei, data)
