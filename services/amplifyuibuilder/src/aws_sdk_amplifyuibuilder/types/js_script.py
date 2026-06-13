"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#JSScript``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplifyuibuilder.errors import DeserializationError

JSScript: TypeAlias = Literal[
    "jsx",
    "tsx",
    "js",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "jsx",
        "tsx",
        "js",
    )
)


def serialize_json(value: JSScript) -> str:
    return value


def deserialize_json(data: str) -> JSScript:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JSScript value: {data!r}")
    return cast(JSScript, data)
