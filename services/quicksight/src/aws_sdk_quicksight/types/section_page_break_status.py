"""Generated from Smithy shape ``com.amazonaws.quicksight#SectionPageBreakStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

SectionPageBreakStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: SectionPageBreakStatus) -> str:
    return value


def deserialize_json(data: str) -> SectionPageBreakStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SectionPageBreakStatus value: {data!r}")
    return cast(SectionPageBreakStatus, data)
