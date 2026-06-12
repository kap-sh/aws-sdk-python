"""Generated from Smithy shape ``com.amazonaws.medialive#H265Profile``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H265 Profile"""
H265Profile: TypeAlias = Literal[
    "MAIN",
    "MAIN_10BIT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MAIN",
        "MAIN_10BIT",
    )
)


def serialize_json(value: H265Profile) -> str:
    return value


def deserialize_json(data: str) -> H265Profile:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H265Profile value: {data!r}")
    return cast(H265Profile, data)
