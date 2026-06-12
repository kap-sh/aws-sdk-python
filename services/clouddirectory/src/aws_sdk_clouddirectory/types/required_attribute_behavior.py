"""Generated from Smithy shape ``com.amazonaws.clouddirectory#RequiredAttributeBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_clouddirectory.errors import DeserializationError

RequiredAttributeBehavior: TypeAlias = Literal[
    "REQUIRED_ALWAYS",
    "NOT_REQUIRED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REQUIRED_ALWAYS",
        "NOT_REQUIRED",
    )
)


def serialize_json(value: RequiredAttributeBehavior) -> str:
    return value


def deserialize_json(data: str) -> RequiredAttributeBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RequiredAttributeBehavior value: {data!r}")
    return cast(RequiredAttributeBehavior, data)
