"""Generated from Smithy shape ``com.amazonaws.quicksight#PanelBorderStyle``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

PanelBorderStyle: TypeAlias = Literal[
    "SOLID",
    "DASHED",
    "DOTTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SOLID",
        "DASHED",
        "DOTTED",
    )
)


def serialize_json(value: PanelBorderStyle) -> str:
    return value


def deserialize_json(data: str) -> PanelBorderStyle:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PanelBorderStyle value: {data!r}")
    return cast(PanelBorderStyle, data)
