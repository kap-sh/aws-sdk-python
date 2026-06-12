"""Generated from Smithy shape ``com.amazonaws.mediatailor#FunctionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediatailor.errors import DeserializationError

"""-- Define Enums"""
FunctionType: TypeAlias = Literal[
    "HTTP_REQUEST",
    "CUSTOM_OUTPUT",
    "SEQUENTIAL_EXECUTOR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HTTP_REQUEST",
        "CUSTOM_OUTPUT",
        "SEQUENTIAL_EXECUTOR",
    )
)


def serialize_json(value: FunctionType) -> str:
    return value


def deserialize_json(data: str) -> FunctionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FunctionType value: {data!r}")
    return cast(FunctionType, data)
