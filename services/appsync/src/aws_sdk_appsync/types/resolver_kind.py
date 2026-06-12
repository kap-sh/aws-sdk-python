"""Generated from Smithy shape ``com.amazonaws.appsync#ResolverKind``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appsync.errors import DeserializationError

ResolverKind: TypeAlias = Literal[
    "UNIT",
    "PIPELINE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNIT",
        "PIPELINE",
    )
)


def serialize_json(value: ResolverKind) -> str:
    return value


def deserialize_json(data: str) -> ResolverKind:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResolverKind value: {data!r}")
    return cast(ResolverKind, data)
