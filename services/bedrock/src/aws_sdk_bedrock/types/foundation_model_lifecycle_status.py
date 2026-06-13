"""Generated from Smithy shape ``com.amazonaws.bedrock#FoundationModelLifecycleStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

FoundationModelLifecycleStatus: TypeAlias = Literal[
    "ACTIVE",
    "LEGACY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "LEGACY",
    )
)


def serialize_json(value: FoundationModelLifecycleStatus) -> str:
    return value


def deserialize_json(data: str) -> FoundationModelLifecycleStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown FoundationModelLifecycleStatus value: {data!r}"
        )
    return cast(FoundationModelLifecycleStatus, data)
