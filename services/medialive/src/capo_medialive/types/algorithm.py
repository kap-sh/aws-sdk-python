"""Generated from Smithy shape ``com.amazonaws.medialive#Algorithm``."""

from typing import Literal, TypeAlias, cast

"""Placeholder documentation for Algorithm"""
Algorithm: TypeAlias = Literal[
    "AES128",
    "AES192",
    "AES256",
]


# --- restJson1 ser/de ---
def serialize_json(value: Algorithm) -> str:
    return value


def deserialize_json(data: str) -> Algorithm:
    return cast(Algorithm, data)
