"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#JSModule``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplifyuibuilder.errors import DeserializationError

JSModule: TypeAlias = Literal[
    "es2020",
    "esnext",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "es2020",
        "esnext",
    )
)


def serialize_json(value: JSModule) -> str:
    return value


def deserialize_json(data: str) -> JSModule:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JSModule value: {data!r}")
    return cast(JSModule, data)
