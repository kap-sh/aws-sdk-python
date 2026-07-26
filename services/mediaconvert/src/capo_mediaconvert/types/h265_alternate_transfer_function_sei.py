"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H265AlternateTransferFunctionSei``."""

from typing import Literal, TypeAlias, cast

"""Enables Alternate Transfer Function SEI message for outputs using Hybrid Log Gamma (HLG) Electro-Optical Transfer Function (EOTF)."""
H265AlternateTransferFunctionSei: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: H265AlternateTransferFunctionSei) -> str:
    return value


def deserialize_json(data: str) -> H265AlternateTransferFunctionSei:
    return cast(H265AlternateTransferFunctionSei, data)
