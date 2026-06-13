"""Generated from Smithy shape ``com.amazonaws.quicksight#Edition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

Edition: TypeAlias = Literal[
    "STANDARD",
    "ENTERPRISE",
    "ENTERPRISE_AND_Q",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD",
        "ENTERPRISE",
        "ENTERPRISE_AND_Q",
    )
)


def serialize_json(value: Edition) -> str:
    return value


def deserialize_json(data: str) -> Edition:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Edition value: {data!r}")
    return cast(Edition, data)
