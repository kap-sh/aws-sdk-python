"""Generated from Smithy shape ``com.amazonaws.quicksight#DecalStyleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

DecalStyleType: TypeAlias = Literal[
    "Manual",
    "Auto",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Manual",
        "Auto",
    )
)


def serialize_json(value: DecalStyleType) -> str:
    return value


def deserialize_json(data: str) -> DecalStyleType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DecalStyleType value: {data!r}")
    return cast(DecalStyleType, data)
