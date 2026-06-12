"""Generated from Smithy shape ``com.amazonaws.guardduty#FilterAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

FilterAction: TypeAlias = Literal[
    "NOOP",
    "ARCHIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOOP",
        "ARCHIVE",
    )
)


def serialize_json(value: FilterAction) -> str:
    return value


def deserialize_json(data: str) -> FilterAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FilterAction value: {data!r}")
    return cast(FilterAction, data)
