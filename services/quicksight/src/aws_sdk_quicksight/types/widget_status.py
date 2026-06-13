"""Generated from Smithy shape ``com.amazonaws.quicksight#WidgetStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

WidgetStatus: TypeAlias = Literal[
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


def serialize_json(value: WidgetStatus) -> str:
    return value


def deserialize_json(data: str) -> WidgetStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WidgetStatus value: {data!r}")
    return cast(WidgetStatus, data)
