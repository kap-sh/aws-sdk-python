"""Generated from Smithy shape ``com.amazonaws.quicksight#ArcThickness``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ArcThickness: TypeAlias = Literal[
    "SMALL",
    "MEDIUM",
    "LARGE",
    "WHOLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SMALL",
        "MEDIUM",
        "LARGE",
        "WHOLE",
    )
)


def serialize_json(value: ArcThickness) -> str:
    return value


def deserialize_json(data: str) -> ArcThickness:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ArcThickness value: {data!r}")
    return cast(ArcThickness, data)
