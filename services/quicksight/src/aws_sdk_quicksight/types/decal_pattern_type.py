"""Generated from Smithy shape ``com.amazonaws.quicksight#DecalPatternType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

DecalPatternType: TypeAlias = Literal[
    "SOLID",
    "DIAGONAL_MEDIUM",
    "CIRCLE_MEDIUM",
    "DIAMOND_GRID_MEDIUM",
    "CHECKERBOARD_MEDIUM",
    "TRIANGLE_MEDIUM",
    "DIAGONAL_OPPOSITE_MEDIUM",
    "DIAMOND_MEDIUM",
    "DIAGONAL_LARGE",
    "CIRCLE_LARGE",
    "DIAMOND_GRID_LARGE",
    "CHECKERBOARD_LARGE",
    "TRIANGLE_LARGE",
    "DIAGONAL_OPPOSITE_LARGE",
    "DIAMOND_LARGE",
    "DIAGONAL_SMALL",
    "CIRCLE_SMALL",
    "DIAMOND_GRID_SMALL",
    "CHECKERBOARD_SMALL",
    "TRIANGLE_SMALL",
    "DIAGONAL_OPPOSITE_SMALL",
    "DIAMOND_SMALL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SOLID",
        "DIAGONAL_MEDIUM",
        "CIRCLE_MEDIUM",
        "DIAMOND_GRID_MEDIUM",
        "CHECKERBOARD_MEDIUM",
        "TRIANGLE_MEDIUM",
        "DIAGONAL_OPPOSITE_MEDIUM",
        "DIAMOND_MEDIUM",
        "DIAGONAL_LARGE",
        "CIRCLE_LARGE",
        "DIAMOND_GRID_LARGE",
        "CHECKERBOARD_LARGE",
        "TRIANGLE_LARGE",
        "DIAGONAL_OPPOSITE_LARGE",
        "DIAMOND_LARGE",
        "DIAGONAL_SMALL",
        "CIRCLE_SMALL",
        "DIAMOND_GRID_SMALL",
        "CHECKERBOARD_SMALL",
        "TRIANGLE_SMALL",
        "DIAGONAL_OPPOSITE_SMALL",
        "DIAMOND_SMALL",
    )
)


def serialize_json(value: DecalPatternType) -> str:
    return value


def deserialize_json(data: str) -> DecalPatternType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DecalPatternType value: {data!r}")
    return cast(DecalPatternType, data)
