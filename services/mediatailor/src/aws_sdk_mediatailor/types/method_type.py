"""Generated from Smithy shape ``com.amazonaws.mediatailor#MethodType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediatailor.errors import DeserializationError

MethodType: TypeAlias = Literal[
    "GET",
    "POST",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GET",
        "POST",
    )
)


def serialize_json(value: MethodType) -> str:
    return value


def deserialize_json(data: str) -> MethodType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MethodType value: {data!r}")
    return cast(MethodType, data)
