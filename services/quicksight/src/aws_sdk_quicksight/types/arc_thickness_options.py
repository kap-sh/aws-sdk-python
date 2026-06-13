"""Generated from Smithy shape ``com.amazonaws.quicksight#ArcThicknessOptions``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ArcThicknessOptions: TypeAlias = Literal[
    "SMALL",
    "MEDIUM",
    "LARGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SMALL",
        "MEDIUM",
        "LARGE",
    )
)


def serialize_json(value: ArcThicknessOptions) -> str:
    return value


def deserialize_json(data: str) -> ArcThicknessOptions:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ArcThicknessOptions value: {data!r}")
    return cast(ArcThicknessOptions, data)
