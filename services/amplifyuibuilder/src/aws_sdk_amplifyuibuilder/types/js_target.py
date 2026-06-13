"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#JSTarget``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplifyuibuilder.errors import DeserializationError

JSTarget: TypeAlias = Literal[
    "es2015",
    "es2020",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "es2015",
        "es2020",
    )
)


def serialize_json(value: JSTarget) -> str:
    return value


def deserialize_json(data: str) -> JSTarget:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JSTarget value: {data!r}")
    return cast(JSTarget, data)
