"""Generated from Smithy shape ``com.amazonaws.pinpoint#Action``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pinpoint.errors import DeserializationError

Action: TypeAlias = Literal[
    "OPEN_APP",
    "DEEP_LINK",
    "URL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OPEN_APP",
        "DEEP_LINK",
        "URL",
    )
)


def serialize_json(value: Action) -> str:
    return value


def deserialize_json(data: str) -> Action:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Action value: {data!r}")
    return cast(Action, data)
