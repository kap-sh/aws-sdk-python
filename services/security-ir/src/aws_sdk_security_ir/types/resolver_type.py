"""Generated from Smithy shape ``com.amazonaws.securityir#ResolverType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_security_ir.errors import DeserializationError

ResolverType: TypeAlias = Literal[
    "AWS",
    "Self",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS",
        "Self",
    )
)


def serialize_json(value: ResolverType) -> str:
    return value


def deserialize_json(data: str) -> ResolverType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResolverType value: {data!r}")
    return cast(ResolverType, data)
