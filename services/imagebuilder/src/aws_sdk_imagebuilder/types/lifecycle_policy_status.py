"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecyclePolicyStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_imagebuilder.errors import DeserializationError

LifecyclePolicyStatus: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
    )
)


def serialize_json(value: LifecyclePolicyStatus) -> str:
    return value


def deserialize_json(data: str) -> LifecyclePolicyStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LifecyclePolicyStatus value: {data!r}")
    return cast(LifecyclePolicyStatus, data)
