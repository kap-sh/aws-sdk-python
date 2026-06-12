"""Generated from Smithy shape ``com.amazonaws.medialive#InputLossImageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Input Loss Image Type"""
InputLossImageType: TypeAlias = Literal[
    "COLOR",
    "SLATE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COLOR",
        "SLATE",
    )
)


def serialize_json(value: InputLossImageType) -> str:
    return value


def deserialize_json(data: str) -> InputLossImageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputLossImageType value: {data!r}")
    return cast(InputLossImageType, data)
