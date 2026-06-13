"""Generated from Smithy shape ``com.amazonaws.quicksight#RelativeFontSize``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

RelativeFontSize: TypeAlias = Literal[
    "EXTRA_SMALL",
    "SMALL",
    "MEDIUM",
    "LARGE",
    "EXTRA_LARGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EXTRA_SMALL",
        "SMALL",
        "MEDIUM",
        "LARGE",
        "EXTRA_LARGE",
    )
)


def serialize_json(value: RelativeFontSize) -> str:
    return value


def deserialize_json(data: str) -> RelativeFontSize:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RelativeFontSize value: {data!r}")
    return cast(RelativeFontSize, data)
