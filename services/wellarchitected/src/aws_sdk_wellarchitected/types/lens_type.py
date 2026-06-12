"""Generated from Smithy shape ``com.amazonaws.wellarchitected#LensType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

LensType: TypeAlias = Literal[
    "AWS_OFFICIAL",
    "CUSTOM_SHARED",
    "CUSTOM_SELF",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS_OFFICIAL",
        "CUSTOM_SHARED",
        "CUSTOM_SELF",
    )
)


def serialize_json(value: LensType) -> str:
    return value


def deserialize_json(data: str) -> LensType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LensType value: {data!r}")
    return cast(LensType, data)
