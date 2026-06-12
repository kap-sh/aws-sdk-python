"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecyclePolicyDetailActionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_imagebuilder.errors import DeserializationError

LifecyclePolicyDetailActionType: TypeAlias = Literal[
    "DELETE",
    "DEPRECATE",
    "DISABLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DELETE",
        "DEPRECATE",
        "DISABLE",
    )
)


def serialize_json(value: LifecyclePolicyDetailActionType) -> str:
    return value


def deserialize_json(data: str) -> LifecyclePolicyDetailActionType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown LifecyclePolicyDetailActionType value: {data!r}"
        )
    return cast(LifecyclePolicyDetailActionType, data)
